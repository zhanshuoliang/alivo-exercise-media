#!/usr/bin/env python3
"""Build the static GIF review page from the verified motion manifest."""

import argparse
import html
from pathlib import Path

from motion_samples import ROOT, load_motion_samples


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=str(ROOT / "motion-preview.html"))
    args = parser.parse_args()
    items = load_motion_samples()
    cards = []
    for item in items:
        name = html.escape(item["name"])
        cid = html.escape(item["catalogId"])
        gif = html.escape("motion/" + item["file"], quote=True)
        still = html.escape(item["sourceStill"], quote=True)
        cards.append(f'''<article class="card">
  <div class="image"><img src="{gif}" width="414" height="414" alt="{name}的循环动作效果试稿"></div>
  <div class="content"><div class="eyebrow">ALIVO · 动态试稿</div><h2>{name}</h2>
    <p class="identity">{cid}</p>
    <div class="links"><a href="{gif}" download>下载 GIF</a><a href="{still}">查看原静态插图</a></div>
  </div>
</article>''')
    page = TEMPLATE.replace("__CARDS__", "\n".join(cards))
    Path(args.out).write_text(page, encoding="utf-8")
    print(f"wrote {args.out}: {len(items)} motion samples")


TEMPLATE = '''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ALIVO 动作 GIF 样例</title>
<style>
:root{color-scheme:light;--ink:#182722;--muted:#66746d;--accent:#245b49;--line:#dfe6e1;--paper:#f5f7f4}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",sans-serif}
header{background:#fff;border-bottom:1px solid var(--line)}.bar{max-width:1040px;margin:auto;padding:16px 22px;display:flex;justify-content:space-between;gap:16px;align-items:center}
.brand{font-weight:800;letter-spacing:.13em}.back{color:var(--accent);text-decoration:none;font-size:14px;font-weight:600}
main{max-width:1040px;margin:auto;padding:46px 22px 64px}.eyebrow{font-size:11px;letter-spacing:.12em;color:var(--accent);font-weight:700}
h1{font-size:clamp(28px,4vw,42px);line-height:1.15;margin:10px 0 12px;letter-spacing:-.035em}h2{font-size:22px;margin:4px 0}
.intro{max-width:720px;color:var(--muted);margin:0 0 28px}.notice{border-left:3px solid #93ad9f;padding:10px 14px;background:#e9f0ea;color:#42554a;font-size:14px;margin:0 0 26px}
.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px}.card{background:#fff;border:1px solid var(--line);border-radius:16px;overflow:hidden;box-shadow:0 8px 24px #1737250a}
.image{aspect-ratio:1;background:#92908f}.image img{display:block;width:100%;height:100%;object-fit:contain}.content{padding:20px 22px 22px}.identity{color:var(--muted);font-size:12px;margin:0 0 15px}
.links{display:flex;gap:18px;flex-wrap:wrap}.links a{color:var(--accent);font-size:14px;font-weight:600;text-decoration:none}.links a:hover,.back:hover{text-decoration:underline}a:focus-visible{outline:3px solid #90b5a3;outline-offset:3px;border-radius:2px}
@media(max-width:650px){main{padding-top:32px}.grid{grid-template-columns:1fr;gap:16px}.bar{padding:14px 18px}main{padding-left:18px;padding-right:18px}}
</style>
</head>
<body>
<header><div class="bar"><div class="brand">ALIVO <span style="font-weight:400;letter-spacing:0;color:#66746d">素材审查</span></div><a class="back" href="catalog-review.html">← 返回动作库</a></div></header>
<main>
  <div class="eyebrow">MOTION PREVIEW · 01</div>
  <h1>动作 GIF 样例</h1>
  <p class="intro">从两个常用动作开始，看看 ALIVO 图片动起来的效果。</p>
  <p class="notice">ALIVO 编辑插图，非动作教学示范。动态试稿由 AI 关键帧与插帧制作，肢体和服装细节可能有轻微变化。</p>
  <section class="grid" aria-label="动作 GIF 样例">
__CARDS__
  </section>
</main>
</body>
</html>'''


if __name__ == "__main__":
    main()
