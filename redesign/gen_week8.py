#!/usr/bin/env python3
import diagrams as D
from genlib import main

MM = "content/week-8/What Multimodal AI Can See Hear and Read.html"
SI = "content/week-8/AI and Scientific Images.html"
DC = "content/week-8/Document Intelligence.html"
TR = "content/week-8/Transcription and Audio Analysis.html"
VD = "content/week-8/Video and Multimodal Workflows.html"

FIGS = [
    dict(fid="fig-w8-modalities", page=MM, loc=r'The Four Modalities', mode="after_p",
         cap="Four research-relevant modalities, the model families that handle each, and what researchers use them for.",
         svg=D.matrix(["Model families", "Research uses"], [
             ("Images", ["Gemini, GPT, Claude (vision)", "figures, microscopy, scans"]),
             ("Audio", ["Whisper, Gemini, AssemblyAI", "interviews, fieldwork, lectures"]),
             ("Documents", ["Vision LLMs, Document AI", "PDFs, archives, tables, forms"]),
             ("Video", ["Gemini, GPT (native video)", "recordings, observation, demos"]),
         ], "The four research modalities",
            "A grid of four modalities — images, audio, documents, video — with model families and research uses.",
            label_w=110)),

    dict(fid="fig-w8-image-zones", page=SI, loc=r'What AI Can Genuinely Help With', mode="after_p",
         cap="AI reads scientific images well for description and trends — but not for pulling exact numbers off axes. CharXiv: 47% AI vs 80% human on real charts.",
         svg=D.columns([
             dict(title="Reliable: describe", kind='good', lines=["Alt text and captions", "Qualitative trends", "Visual comparison", "Spotting obvious features"]),
             dict(title="Unreliable: extract values", kind='bad', lines=["Exact numbers off axes", "Reading chart geometry", "Precise measurements", "Reasoning about scale"]),
         ], "What scientific-image AI can and cannot do",
            "Two zones: reliable description and trend-reading versus unreliable extraction of exact values.")),

    dict(fid="fig-w8-pdf-types", page=DC, loc=r'Why PDFs Are Harder', mode="after_p",
         cap="Three kinds of PDF, and why extraction quality depends on which you have: native text extracts cleanly, scans need OCR, mixed needs page-by-page checking.",
         svg=D.columns([
             dict(title="Native (text layer)", kind='good', lines=["Text stored as characters", "Extracts cleanly", "Most modern PDFs"]),
             dict(title="Scanned (image)", kind='warn', lines=["The page is just a picture", "Needs OCR", "Old papers, archives"]),
             dict(title="Mixed", kind='alt', lines=["Some text, some image", "Patchy extraction", "Check page by page"]),
         ], "Three kinds of PDF",
            "Native, scanned, and mixed PDFs compared by how their text is stored and how well it extracts.")),

    dict(fid="fig-w8-wer", page=TR, loc=r'What the Numbers Mean', mode="after_p",
         cap="Word error rate jumps off clean read speech — meetings, phone audio, and untuned African-language models all cross the line where every transcript needs human review.",
         svg=D.barchart([
             ("Clean read speech", 2.0, 'good'),
             ("Meeting audio", 11.5, 'warn'),
             ("Telephony", 17.7, 'warn'),
             ("isiZulu, untuned", 28.0, 'bad'),
         ], "Word error rate across audio conditions",
            "A bar chart of word error rate rising from clean read speech to untuned African-language transcription.",
            unit='%', threshold=10, thresh_label="≈10%: review needed")),

    dict(fid="fig-w8-native-vs-text", page=VD, loc=r'Native Multimodal vs', mode="after_p",
         cap="Two ways to handle video: a native multimodal model processes sound and vision together; a text-centric pipeline converts to text first and loses what isn't said.",
         svg=D.columns([
             dict(title="Native multimodal", kind='accent', lines=["Audio, image, text together", "One joint model (Gemini, GPT)", "Cross-modal reasoning", "Sees and hears at once"]),
             dict(title="Text-centric pipeline", kind='alt', lines=["Transcribe to text first", "Then a language model", "Loses non-verbal cues", "Each step converts away detail"]),
         ], "Native multimodal versus text-centric",
            "Two architectures: joint multimodal processing versus a transcribe-then-read text pipeline.")),
]

if __name__ == '__main__':
    main(FIGS, "wk8")
