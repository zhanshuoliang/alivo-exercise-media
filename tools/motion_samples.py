"""Read and validate the independently hosted ALIVO motion samples."""

import hashlib
import json
import re
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_motion_samples(root=ROOT):
    manifest = json.loads((root / "motion/manifest.json").read_text(encoding="utf-8"))
    if manifest.get("schemaVersion") != 1 or not isinstance(manifest.get("items"), list):
        raise ValueError("Invalid motion sample manifest")

    metadata = json.loads((root / "catalog/exercise_metadata.json").read_text(encoding="utf-8"))
    bound = {item["catalogId"]: item for item in metadata["media"]}
    seen = set()
    seen_files = set()
    for item in manifest["items"]:
        cid, filename = item["catalogId"], item["file"]
        if (cid in seen or cid not in bound or filename in seen_files or
                not re.fullmatch(r"[a-z0-9_-]+\.gif", filename)):
            raise ValueError(f"Invalid motion sample identity: {cid}")
        seen.add(cid)
        seen_files.add(filename)
        if item.get("license") != "ALIVO-editorial" or item.get("status") != "experimental":
            raise ValueError(f"Invalid motion sample attribution: {cid}")

        still = item["sourceStill"]
        expected_still = "media/" + bound[cid]["localPath"].split("/", 1)[1]
        if (still != expected_still or bound[cid]["license"] != "ALIVO-editorial" or
                item["sourceStillSha256"] != bound[cid]["sha256"]):
            raise ValueError(f"Invalid reference image: {cid}")
        keyframes = item["keyframes"]
        if not re.fullmatch(r"sources/[a-z0-9_-]+\.png", keyframes):
            raise ValueError(f"Invalid keyframe path: {cid}")

        for relative, expected in (("motion/" + filename, item["sha256"]),
                                   (still, item["sourceStillSha256"]),
                                   ("motion/" + keyframes, item["keyframesSha256"])):
            actual = hashlib.sha256((root / relative).read_bytes()).hexdigest()
            if actual != expected:
                raise ValueError(f"SHA-256 mismatch: {relative}")

        with (root / "motion" / filename).open("rb") as image:
            header = image.read(10)
        if header[:6] not in (b"GIF87a", b"GIF89a") or len(header) != 10:
            raise ValueError(f"Invalid GIF: {filename}")
        if struct.unpack("<HH", header[6:10]) != (item["width"], item["height"]):
            raise ValueError(f"GIF dimensions mismatch: {filename}")
    return manifest["items"]
