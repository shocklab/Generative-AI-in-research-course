#!/usr/bin/env python3
import os, re, sys
import diagrams as D

ROOT = "/Users/jonathanshock/Cursor folders/Gen AI in research course/Course materials"
HIST = "content/week-1/History of AI From Neurons to Neural Networks.html"
UNDR = "content/week-1/Understanding How Generative AI Works.html"
LAND = "content/week-1/Current Generative AI Landscape.html"

FIGS = [
    dict(fid="fig-w1-ai-timeline", page=HIST, mode="before",
         loc=r'<h2 class="section-title">[^<]*Pre-History',
         cap="From the Mechanical Turk to generative AI: the eras, the two winters, and the turning points behind today's systems.",
         svg=D.vtimeline([
             ("Pre-history · 1770–1890", [("Von Kempelen's Mechanical Turk chess automaton", 'neutral')]),
             ("Biological roots · 1890–1943", [("Cajal draws neurons; McCulloch–Pitts model", 'neutral')]),
             ("Birth of AI · 1950–1969", [("Turing test; the term 'AI' is coined in 1956", 'accent')]),
             ("Winters & revival · 1970–2006", [("Hype outruns results; two funding winters", 'bad')]),
             ("Statistical turn · 1990–2013", [("Statistics beats hand-written rules", 'good')]),
             ("Deep learning · 2010–2017", [("ImageNet then AlexNet; neural nets take over", 'good')]),
             ("Generative AI · 2018–now", [("Transformers scale: GPT, then ChatGPT", 'accent')]),
         ], "A timeline of AI from 1770 to today",
            "Seven eras from the Mechanical Turk through two AI winters, the statistical turn, deep learning, and the generative-AI era.")),

    dict(fid="fig-w1-three-paradigms", page=HIST, mode="before",
         loc=r'<h2 class="section-title">[^<]*Deep Learning Revolution',
         cap="Three ways a machine can 'know' something: follow hand-written rules, learn statistics from data, or train a deep neural network.",
         svg=D.columns([
             dict(title="Symbolic rules", kind='neutral',
                  lines=["Humans hand-write the logic", "Explicit if-then rules", "Brittle outside its rules"]),
             dict(title="Statistical ML", kind='alt',
                  lines=["Learns patterns from data", "Probabilities, not rules", "Needs many examples"]),
             dict(title="Deep learning", kind='accent',
                  lines=["Many-layered neural nets", "Learns its own features", "Powers generative AI"]),
         ], "Three paradigms of AI",
            "A comparison of symbolic rules, statistical machine learning, and deep learning as three ways of encoding knowledge.")),

    dict(fid="fig-w1-disc-vs-gen", page=UNDR, mode="before",
         loc=r'<h2 class="section-title">[^<]*Key Architectures',
         cap="The core split: discriminative models tell things apart; generative models make new things.",
         svg=D.columns([
             dict(title="Discriminative AI", kind='alt',
                  lines=["Draws boundaries between categories", "Asks: which class is this?", "Example: spam or not spam"]),
             dict(title="Generative AI", kind='accent',
                  lines=["Learns the structure to make new data", "Asks: produce a new example", "Example: write an email, draw an image"]),
         ], "Discriminative versus generative AI",
            "Discriminative AI classifies existing data; generative AI learns the underlying structure to create new data.")),

    dict(fid="fig-w1-three-architectures", page=UNDR, mode="after_p",
         loc=r'Three main architectures power today',
         cap="Three engines behind generative AI — transformers for language, diffusion for images and video, and the older GAN approach.",
         svg=D.columns([
             dict(title="Transformers", kind='accent',
                  lines=["Weighs every word at once", "ChatGPT, Claude, Gemini", "Best for text and code"]),
             dict(title="Diffusion", kind='alt',
                  lines=["Denoise from random noise", "Most image & video models", "Images, audio, video"]),
             dict(title="GANs", kind='neutral',
                  lines=["A forger versus a critic", "Older, sharp images", "Overtaken by diffusion"]),
         ], "Three generative architectures",
            "Transformers, diffusion models, and GANs compared by how they work and what they are best suited to.")),

    dict(fid="fig-w1-modality-map", page=LAND, mode="before",
         loc=r'<h2 class="section-title">[^<]*Large Language Models',
         cap="The generative-AI landscape by output type — the leading model families in each, and what each is best suited to.",
         svg=D.matrix(["Leading families (May 2026)", "Best suited to"], [
             ("Text / LLMs", ["GPT-5.5, Claude, Gemini, DeepSeek", "writing, reasoning, agents, code"]),
             ("Images", ["DALL·E 3, Midjourney, Imagen, FLUX", "figures, illustration, design"]),
             ("Video", ["Sora 2, Veo 3, Runway, Kling", "clips, animation, demonstrations"]),
             ("Code / agents", ["Codex, Claude Code, Cursor, Copilot", "writing and running code"]),
         ], "The generative-AI modality map",
            "A grid of four output modalities — text, images, video, code — with leading model families and their best uses.")),
]


def dump():
    out = os.path.join(ROOT, "redesign", "_wk1_preview")
    os.makedirs(out, exist_ok=True)
    for f in FIGS:
        open(os.path.join(out, f['fid'] + ".svg"), "w", encoding="utf-8").write(f['svg'])
    print("dumped", len(FIGS), "svgs to", out)


def insert():
    for f in FIGS:
        path = os.path.join(ROOT, f['page'])
        src = open(path, encoding='utf-8').read()
        if f'id="{f["fid"]}"' in src:
            print("SKIP (present):", f['fid']); continue
        m = re.search(f['loc'], src)
        if not m:
            print("!! LOCATOR NOT FOUND:", f['fid'], "in", f['page']); continue
        if f['mode'] == 'before':
            idx = m.start()
        elif f['mode'] == 'after_p':
            c = src.find('</p>', m.end()); idx = c + 4 if c != -1 else m.end()
        else:
            idx = m.end()
        fig = f'\n<figure id="{f["fid"]}" class="diagram">{f["svg"]}<figcaption>{f["cap"]}</figcaption></figure>\n'
        open(path, 'w', encoding='utf-8').write(src[:idx] + fig + src[idx:])
        print("OK inserted:", f['fid'])


if __name__ == '__main__':
    (insert if '--insert' in sys.argv else dump)()
