import os
import qrcode
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, KeepTogether, HRFlowable, PageBreak
)
import pymupdf

def build_pdf_offer_letter():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    site_dir = os.path.join(base_dir, "..", "site_1to1")
    doc_dir = os.path.join(site_dir, "assets", "documents")
    os.makedirs(doc_dir, exist_ok=True)

    pdf_path = os.path.join(doc_dir, "Official_Offer_Letter_UCHI_2027_Devendra_Dubey.pdf")
    img_page1 = os.path.join(doc_dir, "offer_letter_page_1.png")
    img_page2 = os.path.join(doc_dir, "offer_letter_page_2.png")
    img_page3 = os.path.join(doc_dir, "offer_letter_page_3.png")
    logo_path = os.path.join(site_dir, "assets", "uchicago_full_logo.png")
    sig_dean_path = os.path.join(doc_dir, "james_nondorf_signature.png")

    qr_data = "https://portal.uchicago.asia?applicantId=UC-2027-89321&doc=OFFER-LETTER-CHEM-2027"
    qr_path = os.path.join(base_dir, "qr_offer_letter.png")
    qr = qrcode.QRCode(box_size=4, border=1)
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="#800000", back_color="white")
    qr_img.save(qr_path)

    # Document setup: A4 with 38pt margins
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=38,
        rightMargin=38,
        topMargin=32,
        bottomMargin=30,
    )

    styles = getSampleStyleSheet()

    # Typography styles
    primary_maroon = colors.HexColor('#800000')
    charcoal = colors.HexColor('#1a1a1a')
    slate_gray = colors.HexColor('#4a5568')
    border_gray = colors.HexColor('#d1d5db')
    bg_light = colors.HexColor('#fcf9f9')

    p1_header_right_style = ParagraphStyle(
        'P1HeaderRight',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=11.2,
        textColor=charcoal,
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=primary_maroon,
        textTransform='uppercase',
        spaceBefore=6,
        spaceAfter=3,
    )

    p1_body_style = ParagraphStyle(
        'P1BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.0,
        leading=13.0,
        textColor=charcoal,
        alignment=4, # Justified
        spaceAfter=8,
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.8,
        leading=12.6,
        textColor=charcoal,
        alignment=4, # Justified
        spaceAfter=6,
    )

    header_right_style = ParagraphStyle(
        'HeaderRight',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10.5,
        alignment=2,
        textColor=charcoal,
    )

    small_text = ParagraphStyle(
        'SmallNotice',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.2,
        leading=9.5,
        textColor=slate_gray,
    )

    elements = []

    # =========================================================================
    # PAGE 1: OFFICIAL LETTER FROM DEAN JAMES G. NONDORF (EXACT PHOTO FORMAT)
    # =========================================================================

    # Header: Logo on left, Vertical rule + Office of College Admissions on right
    if os.path.exists(logo_path):
        p1_logo_img = RLImage(logo_path, width=185, height=39.5)
    else:
        p1_logo_img = Paragraph("<b>THE UNIVERSITY OF CHICAGO</b>", styles['Normal'])

    p1_header_right_text = Paragraph(
        "<b><font color='#800000'>Office of College Admissions</font></b><br/><br/>"
        "1101 East 58th Street<br/>"
        "Chicago, IL 60637<br/><br/>"
        "collegeadmissions@uchicago.edu<br/>"
        "T: 773.702.8650<br/>"
        "F: 773.702.4199",
        p1_header_right_style
    )

    p1_header_table = Table([[p1_logo_img, p1_header_right_text]], colWidths=[310, 209])
    p1_header_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (0, 0), 0),
        ('RIGHTPADDING', (0, 0), (0, 0), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING', (1, 0), (1, 0), 14),
        ('LINEBEFORE', (1, 0), (1, 0), 1.2, colors.HexColor('#b5aea7')),
    ]))
    elements.append(p1_header_table)
    elements.append(Spacer(1, 24))

    # Date
    p1_date = Paragraph("October 16, 2026", ParagraphStyle('P1Date', parent=styles['Normal'], fontName='Helvetica', fontSize=9.5, leading=13, textColor=charcoal))
    elements.append(p1_date)
    elements.append(Spacer(1, 12))

    # Recipient
    p1_recipient = Paragraph(
        "<b>Devendra Dubey</b><br/>"
        "G-704, Lodha Elite, Lodha Heaven<br/>"
        "Nilje, Maharashtra 421204, India<br/>"
        "<font color='#555555' size='8'>Applicant ID: <b>UC-2027-89321</b> &nbsp;|&nbsp; UCID: <b>12489321</b></font>",
        ParagraphStyle('P1Recip', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=12.5, textColor=charcoal)
    )
    elements.append(p1_recipient)
    elements.append(Spacer(1, 14))

    # Salutation
    elements.append(Paragraph("<b>Dear Devendra Dubey,</b>", ParagraphStyle('P1Salute', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.5, leading=13, textColor=charcoal)))
    elements.append(Spacer(1, 8))

    # Body Paragraphs
    let_p1 = (
        "On behalf of the faculty, the Admissions Committee, and the entire academic community of <b>The University of Chicago</b>, "
        "it is my absolute pleasure and distinct honor to offer you admission to the <b>Doctor of Philosophy (Ph.D.) degree program "
        "in Chemistry</b> beginning in the <b>Autumn Quarter 2027</b>."
    )
    elements.append(Paragraph(let_p1, p1_body_style))

    let_p2 = (
        "Admission to the University of Chicago is among the most competitive in the world, extended only to scholars of uncommon "
        "intellect, purpose, and originality. Among thousands of exceptional candidates from across the globe, your dossier stood "
        "out for its profound scientific maturity and rigorous analytical capability. The admissions committee was deeply impressed "
        "by your academic record at the <b>Indian Institute of Technology Gandhinagar (IITGN)</b>, your first-class honors, and the "
        "stellar commendations provided by your faculty referees."
    )
    elements.append(Paragraph(let_p2, p1_body_style))

    let_p3 = (
        "In particular, our faculty selection panel and <b>Professor Alex (Alexander Q.) Cusumano</b> conducted an exhaustive "
        "review of your research portfolio, specifically commending your <b>editor-led computational research project and software architectures</b>. "
        "Professor Cusumano praised the technical elegance, algorithmic depth, and creative execution demonstrated throughout your work. "
        "Reflecting this high praise, <b>Professor Alex Cusumano has officially accepted you into the Cusumano Research Group in the Searle "
        "Chemistry Laboratories</b> as your designated Faculty Research Advisor."
    )
    elements.append(Paragraph(let_p3, p1_body_style))

    let_p4 = (
        "At Chicago, we are committed to ensuring that every doctoral scholar is fully supported throughout their scholarly journey. "
        "I am delighted to confirm that you have been awarded a <b>100% fully funded doctoral fellowship package</b>, guaranteeing full "
        "tuition remission ($20,000 per semester), complete individual U-SHIP health coverage, and an annual living stipend of $36,000 "
        "($3,000 per month). Comprehensive details of your fellowship, departmental placement, and seat locking guarantee are detailed "
        "in the enclosed departmental dossier."
    )
    elements.append(Paragraph(let_p4, p1_body_style))

    let_p5 = (
        "UChicago is an environment where foundational questions are asked and transformative ideas are born. We know that your "
        "scholarly voice and drive will make lasting contributions to our university and the field of chemical sciences. "
        "Please accept our warmest congratulations and our enthusiastic welcome to Hyde Park."
    )
    elements.append(Paragraph(let_p5, p1_body_style))
    elements.append(Spacer(1, 10))

    # Sign-off & Signature
    elements.append(Paragraph("Kind regards,", ParagraphStyle('P1Close', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=12, textColor=charcoal)))
    elements.append(Spacer(1, 4))

    if os.path.exists(sig_dean_path):
        sig_img = RLImage(sig_dean_path, width=96, height=52)
        sig_img.hAlign = 'LEFT'
        elements.append(sig_img)
    elements.append(Spacer(1, 4))

    elements.append(Paragraph(
        "<b>James G. Nondorf</b><br/>"
        "Dean of Admissions and Financial Aid<br/>"
        "The University of Chicago",
        ParagraphStyle('P1Signer', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=charcoal)
    ))

    # Page 1 Footer Note
    elements.append(Spacer(1, 14))
    p1_footer = Table([[
        Paragraph("<font color='#800000'><b>THE UNIVERSITY OF CHICAGO</b></font> • Office of College Admissions • Official Letter of Admission", small_text),
        Paragraph("Page 1 of 3", ParagraphStyle('P1F', parent=small_text, alignment=2))
    ]], colWidths=[420, 99])
    p1_footer.setStyle(TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, primary_maroon),
    ]))
    elements.append(p1_footer)

    # =========================================================================
    # PAGE 2: ADMISSION OFFER, FACULTY ACCEPTANCE & EDITOR PROJECT
    # =========================================================================
    elements.append(PageBreak())

    # Institutional Header Table
    if os.path.exists(logo_path):
        logo_img = RLImage(logo_path, width=170, height=36)
    else:
        logo_img = Paragraph("<b>THE UNIVERSITY OF CHICAGO</b>", styles['Normal'])

    header_text = Paragraph(
        "<b>Division of the Physical Sciences</b><br/>"
        "<b>Department of Chemistry • Doctoral Admissions</b><br/>"
        "Searle Chemistry Laboratories • 5735 S. Ellis Avenue<br/>"
        "Chicago, Illinois 60637, United States<br/>"
        "<font color='#800000'><b>https://uchicago.asia • portal.uchicago.asia</b></font>",
        header_right_style
    )

    header_table = Table([[logo_img, header_text]], colWidths=[200, 319])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    elements.append(header_table)
    elements.append(HRFlowable(width="100%", thickness=2, color=primary_maroon, spaceAfter=8, spaceBefore=4))

    # Reference & Date Bar
    ref_table_data = [
        [
            Paragraph("<b>DOCUMENT REF:</b> UCHI-PSD-CHEM-OFFER-2027-89321", ParagraphStyle('R1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, textColor=primary_maroon)),
            Paragraph("<b>DATE OF ISSUANCE:</b> October 16, 2026", ParagraphStyle('R2', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, alignment=2, textColor=charcoal))
        ]
    ]
    ref_table = Table(ref_table_data, colWidths=[280, 239])
    ref_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (-1, -1), bg_light),
        ('BOX', (0, 0), (-1, -1), 0.5, border_gray),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(ref_table)
    elements.append(Spacer(1, 8))

    # Candidate Dossier Block Table
    candidate_info = [
        [
            Paragraph("<b>CANDIDATE / ADMITTEE:</b>", ParagraphStyle('C1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.5, textColor=primary_maroon)),
            Paragraph("<b>DEVENDRA DUBEY</b> (Devendra Dubey Biswambharnath Geeta)", ParagraphStyle('C2', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, textColor=charcoal))
        ],
        [
            Paragraph("<b>APPLICANT IDENTIFIER:</b>", ParagraphStyle('C1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.5, textColor=primary_maroon)),
            Paragraph("Application ID: <b>UC-2027-89321</b> &nbsp;|&nbsp; UCID: <b>12489321</b> &nbsp;|&nbsp; Registered Email: <b>dubey351dev@gmail.com</b>", ParagraphStyle('C2', parent=styles['Normal'], fontName='Helvetica', fontSize=7.8, textColor=charcoal))
        ],
        [
            Paragraph("<b>RESIDENTIAL ADDRESS:</b>", ParagraphStyle('C1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.5, textColor=primary_maroon)),
            Paragraph("G-704, Lodha Elite, Lodha Heaven, Nilje, Maharashtra 421204, India", ParagraphStyle('C2', parent=styles['Normal'], fontName='Helvetica', fontSize=7.8, textColor=charcoal))
        ],
        [
            Paragraph("<b>OFFERED PROGRAM:</b>", ParagraphStyle('C1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.5, textColor=primary_maroon)),
            Paragraph("<b>Doctor of Philosophy (Ph.D.) in Chemistry</b> &nbsp;(Track: Computational Chemistry &amp; Catalysis)", ParagraphStyle('C2', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.2, textColor=charcoal))
        ],
        [
            Paragraph("<b>MATRICULATION TERM:</b>", ParagraphStyle('C1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.5, textColor=primary_maroon)),
            Paragraph("Autumn Quarter 2027 &nbsp;|&nbsp; Doctoral Cohort Move-In: <b>August 2027</b>", ParagraphStyle('C2', parent=styles['Normal'], fontName='Helvetica', fontSize=8, textColor=charcoal))
        ]
    ]
    cand_table = Table(candidate_info, colWidths=[130, 389])
    cand_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f9fafb')),
        ('BOX', (0, 0), (-1, -1), 0.5, border_gray),
        ('INNERGRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#e5e7eb')),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(cand_table)
    elements.append(Spacer(1, 10))

    # Formal Offer Salutation & Body
    elements.append(Paragraph("<b>Dear Mr. Devendra Dubey,</b>", ParagraphStyle('Salutation', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.5, textColor=charcoal, spaceAfter=5)))

    p1 = (
        "On behalf of the Graduate Faculty of the Department of Chemistry and the Division of the Physical Sciences "
        "at <b>The University of Chicago</b>, it is our greatest pleasure and honor to offer you admission to the "
        "<b>Doctor of Philosophy (Ph.D.) degree program in Chemistry</b> beginning in the <b>Autumn Quarter 2027</b> "
        "(formal doctoral matriculation in August 2027)."
    )
    elements.append(Paragraph(p1, body_style))

    p2 = (
        "Admission to our graduate program is intensely selective, granted only to candidates demonstrating exceptional "
        "intellectual independence, rigorous scientific aptitude, and profound research promise. Your outstanding master's "
        "record at the Indian Institute of Technology Gandhinagar (IITGN, CGPA 8.46 / 10.00 First Class with Distinction), "
        "supported by the highest recommendations from your faculty referees, distinguished your file among thousands of "
        "global applicants."
    )
    elements.append(Paragraph(p2, body_style))

    # Special Commendation Box for Editor-Led Project & Prof. Alex Cusumano
    commendation_content = [
        [
            Paragraph(
                "<b>FACULTY ACCEPTANCE &amp; COMMENDATION OF EDITOR-LED PROJECT</b><br/>"
                "The Admissions Committee and Faculty Selection Panel conducted a comprehensive evaluation of your scholarly "
                "portfolio, specifically giving thorough review to your <b>editor-led computational research project and software architectures</b>. "
                "<b>Professor Alex (Alexander Q.) Cusumano</b>, Assistant Professor of Chemistry (Computational &amp; Theoretical Chemistry, "
                "Molecular Dynamics, Catalysis), was extraordinarily impressed by the technical depth, algorithmic rigor, and creative "
                "methodological execution demonstrated across your editor-led project.<br/><br/>"
                "Reflecting this high praise, <b>Professor Alex Cusumano has officially accepted you into the Cusumano Research Group</b> "
                "in the Searle Chemistry Laboratories as your designated Faculty Research Advisor. Both Professor Cusumano and our "
                "departmental faculty are tremendously excited to meet and mentor you as you commence your doctoral investigations "
                "in computational chemistry and reaction catalysis this coming semester.",
                ParagraphStyle('CommendText', parent=styles['Normal'], fontName='Helvetica', fontSize=8.3, leading=12, textColor=charcoal)
            )
        ]
    ]
    commend_table = Table(commendation_content, colWidths=[519])
    commend_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#fff7f7')),
        ('BOX', (0, 0), (-1, -1), 1, primary_maroon),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(commend_table)
    elements.append(Spacer(1, 8))

    # Summary Card for Placement
    placement_data = [
        [
            Paragraph("<b>Research Advisor:</b>", ParagraphStyle('PL1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.8, textColor=primary_maroon)),
            Paragraph("Prof. Alex (Alexander Q.) Cusumano, Ph.D. — Assistant Professor of Chemistry", ParagraphStyle('PL2', parent=styles['Normal'], fontName='Helvetica', fontSize=8, textColor=charcoal))
        ],
        [
            Paragraph("<b>Research Group:</b>", ParagraphStyle('PL1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.8, textColor=primary_maroon)),
            Paragraph("The Cusumano Research Group • Computational &amp; Theoretical Chemistry Laboratory", ParagraphStyle('PL2', parent=styles['Normal'], fontName='Helvetica', fontSize=8, textColor=charcoal))
        ],
        [
            Paragraph("<b>Laboratory Facility:</b>", ParagraphStyle('PL1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.8, textColor=primary_maroon)),
            Paragraph("Searle Chemistry Laboratories, 5735 S. Ellis Ave, Chicago, IL 60637", ParagraphStyle('PL2', parent=styles['Normal'], fontName='Helvetica', fontSize=8, textColor=charcoal))
        ]
    ]
    placement_table = Table(placement_data, colWidths=[120, 399])
    placement_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (-1, -1), bg_light),
        ('BOX', (0, 0), (-1, -1), 0.5, border_gray),
        ('INNERGRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#e5e7eb')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(placement_table)

    # Page 2 Footer Note
    elements.append(Spacer(1, 14))
    p2_footer = Table([[
        Paragraph("<font color='#800000'><b>THE UNIVERSITY OF CHICAGO</b></font> • Division of the Physical Sciences • Official Admissions Offer &amp; Fellowship Grant", small_text),
        Paragraph("Page 2 of 3", ParagraphStyle('P2F', parent=small_text, alignment=2))
    ]], colWidths=[420, 99])
    p2_footer.setStyle(TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, primary_maroon),
    ]))
    elements.append(p2_footer)

    # =========================================================================
    # PAGE 3: FINANCIAL FELLOWSHIP, TUITION, STIPEND, DEPOSIT TERMS & SIGNATURES
    # =========================================================================
    elements.append(PageBreak())

    # Mini Header on Page 3
    p3_header = Table([[
        Paragraph("<b>THE UNIVERSITY OF CHICAGO</b> &nbsp;•&nbsp; Official Doctoral Award &amp; Enrollment Terms", ParagraphStyle('P3H', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, textColor=primary_maroon)),
        Paragraph("Ref: <b>UCHI-PSD-CHEM-OFFER-2027-89321</b>", ParagraphStyle('P3R', parent=styles['Normal'], fontName='Helvetica', fontSize=7.5, alignment=2, textColor=slate_gray))
    ]], colWidths=[360, 159])
    p3_header.setStyle(TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LINEBELOW', (0, 0), (-1, -1), 1, primary_maroon),
    ]))
    elements.append(p3_header)
    elements.append(Spacer(1, 8))

    elements.append(Paragraph("<b>COMPREHENSIVE FINANCIAL AWARD &amp; DOCTORAL FELLOWSHIP PACKAGE</b>", section_heading))
    p_fin = (
        "The University of Chicago is steadfastly committed to ensuring that every doctoral scholar is fully supported. "
        "Throughout your graduate tenure in good academic standing, you are awarded an institutionally guaranteed "
        "fellowship package covering your complete tuition, mandatory health insurance, and annual living expenses:"
    )
    elements.append(Paragraph(p_fin, body_style))

    # Financial Breakdown Table
    fin_data = [
        [
            Paragraph("<b>AWARD COMPONENT</b>", ParagraphStyle('FH1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.5, textColor=colors.white)),
            Paragraph("<b>FUNDING RATE &amp; COVERAGE</b>", ParagraphStyle('FH2', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.5, textColor=colors.white)),
            Paragraph("<b>FINANCIAL STATUS &amp; DISBURSEMENT TERMS</b>", ParagraphStyle('FH3', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.5, textColor=colors.white))
        ],
        [
            Paragraph("<b>Full Tuition &amp; Academic Fees</b>", ParagraphStyle('FD1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, textColor=charcoal)),
            Paragraph("<b>$20,000.00 USD</b> / Semester<br/><font color='#666' size='7'>($60,000.00 / academic year)</font>", ParagraphStyle('FD2', parent=styles['Normal'], fontName='Helvetica', fontSize=8, textColor=charcoal)),
            Paragraph("<b>100% Fully Funded</b> via Physical Sciences Division Tuition Remission Fellowship. <b>Zero student tuition liability.</b>", ParagraphStyle('FD3', parent=styles['Normal'], fontName='Helvetica', fontSize=8, textColor=primary_maroon))
        ],
        [
            Paragraph("<b>Doctoral Living Stipend</b>", ParagraphStyle('FD1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, textColor=charcoal)),
            Paragraph("<b>$3,000.00 USD</b> / Month<br/><font color='#666' size='7'>($36,000.00 annual stipend)</font>", ParagraphStyle('FD2', parent=styles['Normal'], fontName='Helvetica', fontSize=8, textColor=charcoal)),
            Paragraph("Funded via Graduate Research Assistantship (GRA) under Cusumano Lab; disbursed bi-weekly directly to candidate's account.", ParagraphStyle('FD3', parent=styles['Normal'], fontName='Helvetica', fontSize=8, textColor=charcoal))
        ],
        [
            Paragraph("<b>U-SHIP Health Coverage</b>", ParagraphStyle('FD1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, textColor=charcoal)),
            Paragraph("<b>100% Comprehensive</b><br/><font color='#666' size='7'>Individual Platinum Plan</font>", ParagraphStyle('FD2', parent=styles['Normal'], fontName='Helvetica', fontSize=8, textColor=charcoal)),
            Paragraph("Full annual premium paid directly by the Division of the Physical Sciences; comprehensive medical, dental, and vision.", ParagraphStyle('FD3', parent=styles['Normal'], fontName='Helvetica', fontSize=8, textColor=charcoal))
        ],
        [
            Paragraph("<b>Seat Confirmation Deposit</b>", ParagraphStyle('FD1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, textColor=charcoal)),
            Paragraph("<b>$6,200.00 USD</b><br/><font color='#800000' size='7'><b>Due: Nov 11, 2026</b></font>", ParagraphStyle('FD2', parent=styles['Normal'], fontName='Helvetica', fontSize=8, textColor=charcoal)),
            Paragraph("<b>100% Reimbursable within 90 days</b> of semester commencement; <b>100% Refundable in 90 business days</b> if visa issue occurs.", ParagraphStyle('FD3', parent=styles['Normal'], fontName='Helvetica', fontSize=8, textColor=primary_maroon))
        ]
    ]
    fin_table = Table(fin_data, colWidths=[130, 120, 269])
    fin_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BACKGROUND', (0, 0), (-1, 0), primary_maroon),
        ('BOX', (0, 0), (-1, -1), 0.5, border_gray),
        ('INNERGRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#e5e7eb')),
        ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#ffffff')),
        ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#fcfcfc')),
        ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor('#ffffff')),
        ('BACKGROUND', (0, 4), (-1, 4), colors.HexColor('#fffcfc')),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    elements.append(fin_table)
    elements.append(Spacer(1, 8))

    # Seat Locking Deposit Reimbursable & Refundable Detailed Clause
    elements.append(Paragraph("<b>TERMS OF SEAT LOCKING DEPOSIT: 90-DAY REIMBURSEMENT &amp; GUARANTEED REFUND POLICY</b>", section_heading))
    p_deposit_terms = (
        "To reserve and officially lock your graduate research placement in the Cusumano Laboratory, admitted candidates "
        "submit a Ph.D. Matriculation Seat Confirmation Deposit of <b>$6,200.00 USD</b> by the priority deadline of <b>November 11, 2026</b>. "
        "The University maintains the following institutional guarantee governing this deposit:<br/>"
        "• <b>Full Reimbursability within 90 Days of Semester Start</b>: The entire $6,200.00 USD seat locking fee is <b>100% reimbursable within 90 days</b> "
        "from the formal commencement of the Autumn Quarter (August 2027). The full amount will be credited back directly to your student Bursar account "
        "and disbursed alongside your doctoral fellowship stipend.<br/>"
        "• <b>Full Refundability within 90 Business Days for Unforeseen Travel / Visa Complications</b>: In the unforeseen event of visa denial, "
        "administrative visa processing cancellation, international travel restrictions, or non-enrollment / non-admission due to extenuating "
        "circumstances beyond the candidate's control, <b>the $6,200.00 USD seat locking deposit is 100% refundable within 90 business days</b> upon the "
        "submission of your written notification and supporting documentation to the Division of the Physical Sciences Admissions Office."
    )
    elements.append(Paragraph(p_deposit_terms, body_style))
    elements.append(Spacer(1, 4))

    # Acceptance Instructions & Next Steps
    p_next_steps = (
        "<b>NEXT STEPS TO ACCEPT &amp; CONFIRM MATRICULATION:</b><br/>"
        "1. Log in to your secure <b>Applicant Status Portal</b> at <b>https://portal.uchicago.asia?applicantId=UC-2027-89321</b>.<br/>"
        "2. Review your admission dossier, faculty advisor acceptance card, and pre-authorized Discover payment mandate.<br/>"
        "3. Complete your enrollment confirmation and deposit submission by the <b>Priority Deadline: November 11, 2026</b>.<br/>"
        "4. Your Form I-20 Certificate of Eligibility for Nonimmigrant Student Status (F-1) will be issued promptly by the Office of International Affairs (OIA)."
    )
    elements.append(Paragraph(p_next_steps, body_style))
    elements.append(Spacer(1, 6))

    # Formal Signatures Block
    sig_content = [
        [
            Paragraph(
                "<b>Prof. Alex (Alexander Q.) Cusumano, Ph.D.</b><br/>"
                "<font color='#555' size='7.5'>Assistant Professor of Chemistry<br/>"
                "Principal Investigator, Cusumano Research Group<br/>"
                "Searle Chemistry Laboratories • The University of Chicago</font>",
                ParagraphStyle('S1', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=10.5)
            ),
            Paragraph(
                "<b>Angela V. Olinto, Ph.D.</b><br/>"
                "<font color='#555' size='7.5'>Dean of the Division of the Physical Sciences<br/>"
                "Albert A. Michelson Distinguished Service Professor<br/>"
                "The University of Chicago</font>",
                ParagraphStyle('S2', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=10.5)
            ),
            RLImage(qr_path, width=54, height=54) if os.path.exists(qr_path) else Paragraph("QR", styles['Normal'])
        ]
    ]
    sig_table = Table(sig_content, colWidths=[205, 235, 79])
    sig_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, border_gray),
    ]))
    elements.append(sig_table)

    # Official Seal & Page 3 Footer
    elements.append(Spacer(1, 10))
    p3_footer = Table([[
        Paragraph("<font color='#800000'><b>CRESCAT SCIENTIA; VITA EXCOLATUR</b></font> • The University of Chicago • Division of the Physical Sciences", small_text),
        Paragraph("Page 3 of 3", ParagraphStyle('P3F', parent=small_text, alignment=2))
    ]], colWidths=[420, 99])
    p3_footer.setStyle(TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, primary_maroon),
    ]))
    elements.append(p3_footer)

    # Build the PDF
    doc.build(elements)
    print(f"Generated Official Offer Letter PDF at {pdf_path}")

    # Render high-resolution PNG previews using PyMuPDF
    pdf_doc = pymupdf.open(pdf_path)
    print(f"Total Pages in generated PDF: {len(pdf_doc)}")
    
    p1 = pdf_doc[0]
    pix1 = p1.get_pixmap(dpi=144)
    pix1.save(img_page1)
    print(f"Rendered Page 1 PNG preview at {img_page1} ({pix1.width}x{pix1.height})")

    if len(pdf_doc) > 1:
        p2 = pdf_doc[1]
        pix2 = p2.get_pixmap(dpi=144)
        pix2.save(img_page2)
        print(f"Rendered Page 2 PNG preview at {img_page2} ({pix2.width}x{pix2.height})")

    if len(pdf_doc) > 2:
        p3 = pdf_doc[2]
        pix3 = p3.get_pixmap(dpi=144)
        pix3.save(img_page3)
        print(f"Rendered Page 3 PNG preview at {img_page3} ({pix3.width}x{pix3.height})")

if __name__ == "__main__":
    build_pdf_offer_letter()
    print("Offer letter built successfully!")
