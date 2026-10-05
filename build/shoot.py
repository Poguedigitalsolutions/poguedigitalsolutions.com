"""Full-page screenshots of every page at desktop and mobile widths, with the
scroll-reveal animation forced to its finished state so nothing is hidden."""
import asyncio, sys
from playwright.async_api import async_playwright

OUT = "/tmp/claude-0/-home-claude/ad3c65ec-f2bb-5303-8454-84ff2709139b/scratchpad/shots"
PAGES = sys.argv[1:] or ["index", "solutions", "assessments", "about", "contact"]

async def main():
    import os; os.makedirs(OUT, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name in PAGES:
            for label, w, h in [("desktop", 1440, 900), ("mobile", 390, 844)]:
                pg = await b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1,
                                      reduced_motion="reduce")
                errors = []
                pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
                pg.on("pageerror", lambda e: errors.append(str(e)))
                await pg.goto(f"http://127.0.0.1:8787/{name}.html", wait_until="networkidle")
                # scroll through so lazy images load, then back to top
                await pg.evaluate("""async () => { for (let y=0; y<document.body.scrollHeight; y+=600) { window.scrollTo(0,y); await new Promise(r=>setTimeout(r,40)); } window.scrollTo(0,0); }""")
                await pg.wait_for_timeout(800)
                await pg.screenshot(path=f"{OUT}/{name}-{label}.png", full_page=True)
                # viewport-only shot of the top (what a visitor sees first)
                await pg.screenshot(path=f"{OUT}/{name}-{label}-fold.png")
                dims = await pg.evaluate("({w: document.documentElement.scrollWidth, h: document.documentElement.scrollHeight})")
                print(name, label, dims, "errors:", errors)
                await pg.close()
        await b.close()
asyncio.run(main())
