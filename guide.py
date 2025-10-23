"""
ByteRead Submission Guide Processor
This script holds the complete content of the Article Submission Guide in 
Markdown format, making it easily editable and processable using Python.
It also includes functionality to generate a PDF document using the reportlab library.
"""

GUIDE_MARKDOWN = """
# **ByteRead** Official Article Submission Guide

*Guiding the next generation of analysis at the convergence of AI, Biology, and Medicine.*

---

## 1. ByteRead's Mission and Editorial Tone

**ByteRead** publishes concise, high-impact analysis focused exclusively on the strategic intersection of **Artificial Intelligence (AI), Biology/Neuroscience, and Medicine**. Our goal is to transform complex, foundational research into clear, accessible, and forward-looking reports for a professional audience.

### 1.1 Tone and Style Requirements
* **Analytic and Objective:** Avoid conversational or sensational language. The tone should be authoritative, evidence-based, and focused on translating scientific findings into strategic insights.
* **Clarity is King:** Simplify complexity without sacrificing accuracy. Define technical jargon clearly. Assume the reader is highly intelligent but not necessarily specialized in your narrow field.
* **Length:** Submissions are typically **800–1,500 words** (excluding citations). Conciseness is valued.

---

## 2. Article Structure and Content

All submissions must follow the standard journalistic structure, ensuring a smooth, logical flow from broad topic to specific conclusion.

### 2.1 Mandatory Structural Elements
* **Title:** Clear, engaging, and accurately reflecting the content (max 10 words).
* **Abstract/Summary Paragraph:** A single paragraph (max 150 words) placed before the main body, summarizing the core challenge, the research discussed, and the key takeaway.
* **Introduction:** Clearly define the domain and the "grand challenge" the article addresses. Set the stage for convergence.
* **Body Paragraphs:** Use H2 and H3 headings to logically divide the analysis (e.g., I. Computational Foundations, A. Autonomous Labs). Each section must be **analytical**, not purely descriptive.
* **Conclusion/Outlook:** Briefly summarize the findings and offer a strategic perspective on future research or policy implications. Do not introduce new concepts here.

### 2.2 Author and Metadata Submission
Authors must provide the following separate metadata upon submission:
1.  **Full Author Name(s):** Include current affiliation or primary professional role.
2.  **Short Biography:** A 50-word biography for each author.
3.  **Suggested Keywords:** Up to five keywords for search optimization (e.g., genomics, large language models, neuro-AI).

---

## 3. Sourcing and Citation Guidelines

**ByteRead** is committed to grounding its analysis in primary research and authoritative sources.

### 3.1 Citation Format
* Use in-text, bracketed numbers to reference your sources (e.g., [1], [2]).
* The list of sources should be titled **"Works Cited"** and placed at the end of the article.
* **MANDATORY:** Every citation must be a full, accessible web link (URI) to the original paper, press release, or report. Do not cite secondary news reports unless the primary source is inaccessible.

### 3.2 Example of a Correct Citation Entry

| Column | Content |
| :--- | :--- |
| **Correct Format** | [1] Title of Research Paper or Report, Author(s), Publication Journal/Source, Year. https://full-working-link-to-source.com/document |

---

## 4. Image and Multimedia Requirements

Images must serve an instructional purpose (e.g., charts, diagrams, or scientific illustrations) and adhere strictly to copyright law.

### 4.1 Image Link Guidelines
* **ByteRead** does not host image files directly from authors. You must provide a **direct, stable URL** for any external image you wish to include.
* **Do not use base64 data, local file paths, or private storage links.**
* All images must be accompanied by a descriptive **Caption** and a clear **Credit/Source** line.

---

## 5. Legal and Ethical Policy on Sources and Content

### 5.1 Plagiarism Policy
**Zero Tolerance:** **ByteRead** maintains a zero-tolerance policy for plagiarism. Plagiarism includes:
i.  Presenting someone else's work, ideas, or words as your own without proper attribution.
ii. Using copyrighted text without enclosing it in quotation marks and citing the source, or without securing explicit permission where required.

Any submission found to contain plagiarized material will be **rejected immediately** and the author may be banned from future submissions.

### 5.2 Copyright and Fair Use of Sources
Authors are solely responsible for ensuring that all materials submitted comply with copyright law.

* **Textual Content:** All text must be original or appropriately quoted and attributed. You must rely on **summarization and analysis** of sources, not wholesale reproduction.
* **Image Copyright (Crucial):** You **must** possess the necessary rights or licenses for every image linked. Acceptable sources are limited to:
    * (a) Images the author created and holds the copyright to.
    * (b) Images released under an explicit **Creative Commons (CC) license** (e.g., CC BY, CC BY-SA). The specific license must be noted in the Credit line.
    * (c) Images explicitly designated as **Public Domain**.
    * (d) Images used under legally sound **Fair Use / Fair Dealing** provisions (e.g., using a small, low-resolution thumbnail solely for non-commercial educational critique or analysis). **Note:** Reliance on Fair Use is subject to stringent editorial review and is discouraged for commercial or non-critical use.
* **Prohibited Use:** Content scraped from commercial websites, proprietary research databases, or private social media platforms without explicit permission is strictly prohibited.

---
*Submitting an article confirms the author's acceptance of and adherence to all policies detailed in this guide, including full responsibility for the originality and legal standing of all submitted content.*
"""

# --- PDF GENERATION FUNCTION USING REPORTLAB ---

# Note: ReportLab is used here to demonstrate PDF generation capability.
# For complex Markdown-to-PDF conversion, external libraries like 'markdown' and 
# advanced ReportLab features are usually required. This provides a structural
# representation with the requested branding.
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER
    REPORTLAB_AVAILABLE = True
except ImportError:
    # Set flag if reportlab is not installed in the environment
    REPORTLAB_AVAILABLE = False
    print("Warning: reportlab library not found. PDF generation function will not work.")


# Define the ByteRead Blue color (approximated from text-blue-800: RGB 30, 64, 175)
BYTEREAD_BLUE = colors.Color(30/255.0, 64/255.0, 175/255.0)

def apply_reportlab_styling(text):
    """
    Replaces Markdown ** with ReportLab rich text for bold and the ByteRead blue color.
    Uses split/join to ensure opening and closing tags are correctly paired.
    """
    # Split the text by the Markdown bold marker '**'
    parts = text.split('**')
    styled_text = []
    
    # Iterate over parts, alternating between normal and styled text
    for i, part in enumerate(parts):
        if i % 2 == 1:
            # Odd parts (1, 3, 5...) are inside the bold markers, apply styling
            # Using specific hex color code in rich text tag
            styled_text.append(f'<font color="#1E40AF"><b>{part}</b></font>')
        else:
            # Even parts (0, 2, 4...) are outside the bold markers, keep plain
            styled_text.append(part)
            
    return "".join(styled_text)


def generate_pdf(filename="ByteRead_Submission_Guide.pdf"):
    """
    Generates a PDF document from the GUIDE_MARKDOWN content using reportlab.
    
    The function focuses on recreating the specific branding and structural 
    elements requested (colored title, bold sections).
    """
    if not REPORTLAB_AVAILABLE:
        print(f"Cannot generate PDF: reportlab is not installed.")
        return

    # Basic Document Setup
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            rightMargin=50, leftMargin=50,
                            topMargin=50, bottomMargin=50)
    
    styles = getSampleStyleSheet()
    Story = []

    # --- Custom Styles ---
    styles.add(ParagraphStyle(name='TitleStyle',
                              fontSize=24,
                              leading=30,
                              alignment=TA_CENTER,
                              fontName='Helvetica-Bold'))
    
    styles.add(ParagraphStyle(name='H1_Brand',
                              fontSize=24,
                              leading=30,
                              alignment=TA_CENTER,
                              fontName='Helvetica-Bold',
                              textColor=BYTEREAD_BLUE))

    styles.add(ParagraphStyle(name='H2Style',
                              fontSize=16,
                              leading=20,
                              spaceAfter=12,
                              fontName='Helvetica-Bold'))
    
    styles.add(ParagraphStyle(name='H3Style',
                              fontSize=12,
                              leading=14,
                              spaceAfter=8,
                              fontName='Helvetica-Bold'))
    
    styles.add(ParagraphStyle(name='NormalStyle',
                              fontSize=10,
                              leading=12,
                              spaceAfter=6))
    
    styles.add(ParagraphStyle(name='EmphasisStyle',
                              fontSize=10,
                              leading=12,
                              spaceAfter=6,
                              textColor=BYTEREAD_BLUE,
                              fontName='Helvetica-Bold'))

    # --- Content Flow (Simplified Parsing) ---
    
    # 1. Title (with color on 'ByteRead')
    # The title text already uses the rich text color tag
    Story.append(Paragraph('<font color="#1E40AF"><b>ByteRead</b></font> Official Article Submission Guide', styles['TitleStyle']))
    Story.append(Paragraph(GUIDE_MARKDOWN.split('\n')[2], styles['TitleStyle'])) # Subtitle
    Story.append(Spacer(1, 24))


    # 2. Add content section-by-section (simplified for demonstration)
    sections = GUIDE_MARKDOWN.split('---')[1:] # Skip header
    
    # Process each section based on the structure defined in the Markdown
    for section_content in sections:
        lines = section_content.strip().split('\n')
        
        # Skip empty sections
        if not lines:
            continue

        for line in lines:
            line = line.strip()
            
            if not line:
                continue # Skip truly empty lines

            if line.startswith('## '):
                # H2 Section Header
                Story.append(Spacer(1, 12))
                Story.append(Paragraph(line[3:], styles['H2Style']))
            elif line.startswith('### '):
                # H3 Section Header
                Story.append(Spacer(1, 6))
                Story.append(Paragraph(line[4:], styles['H3Style']))
            elif line.startswith('*') or line.startswith('1.') or line.startswith('i.'):
                # List items (Robust handling: strip marker before styling)
                
                # 1. Determine the content by removing the list marker from the raw line.
                raw_content = line
                if line.startswith('*'):
                    # Handles '* content'
                    raw_content = line[1:].lstrip()
                elif line[0].isdigit() and line[1] == '.': 
                    # Covers numbered list items like '1.', '2.'
                    raw_content = line[2:].lstrip()
                elif line.startswith('i.'): 
                    # Covers Roman numeral list items like 'i.'
                    raw_content = line[2:].lstrip()
                
                # 2. Apply rich text styling to the clean content.
                text = apply_reportlab_styling(raw_content)
                
                # 3. Add the bullet point explicitly.
                Story.append(Paragraph(f"• {text}", styles['NormalStyle']))
                
            elif line.startswith('| Column'):
                # Handle Table (Simplified: only takes the data row)
                try:
                    # Apply styling to the "Correct Format" header
                    table_data = [
                        [Paragraph(apply_reportlab_styling('**Correct Format**'), styles['H3Style'])],
                        [Paragraph(lines[lines.index(line) + 3].split('|')[2].strip(), styles['NormalStyle'])]
                    ]
                    table = Table(table_data, colWidths=[400])
                    table.setStyle(TableStyle([
                        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke)
                    ]))
                    Story.append(Spacer(1, 12))
                    Story.append(table)
                    Story.append(Spacer(1, 12))
                except IndexError:
                    pass # Table structure failed to parse
            
            else:
                # Normal paragraph text (including those starting with **).
                text = apply_reportlab_styling(line)
                Story.append(Paragraph(text, styles['NormalStyle']))
        
        Story.append(Spacer(1, 18))

    # Build the document
    doc.build(Story)
    print(f"\nPDF successfully generated as: {filename}")


def print_guide():
    """Prints the entire submission guide content."""
    print(GUIDE_MARKDOWN)

def get_section(section_number):
    """
    Retrieves a specific section based on its number (e.g., '1' for Mission).
    Note: This is a basic implementation and assumes numbered sections.
    """
    sections = GUIDE_MARKDOWN.split('---')
    target_section = None
    
    # Locate the target section by number
    for section in sections:
        # Check if the section starts with the target number and a period/space
        if section.strip().startswith(f"## {section_number}."):
            target_section = section.strip()
            break

    if target_section:
        return target_section
    else:
        return f"Error: Section {section_number} not found."

if __name__ == "__main__":
    # Example usage: Prints the entire guide and then extracts Section 5
    print("--- ByteRead Official Article Submission Guide ---\n")
    print_guide()
    print("\n\n--- Example of Retrieving Section 5 (Legal and Ethical Policy) ---\n")
    print(get_section('5'))
    
    # Example usage: Generate the PDF
    # Note: This line will only successfully execute if the reportlab library is available.
    print("\n\n--- Attempting to Generate PDF ---\n")
    generate_pdf()
