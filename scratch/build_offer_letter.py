import os
import qrcode
from PIL import Image as PILImage, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, PageBreak
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
    shield_path = os.path.join(site_dir, "assets", "uchicago_shield_crest.png")
    if not os.path.exists(shield_path):
        shield_path = os.path.join(site_dir, "assets", "crest.png")

    sig_dean_path = os.path.join(doc_dir, "james_nondorf_signature.png")

    qr_data = "https://uchicago.asia/portal.html?applicantId=UC-2027-89321&doc=OFFER-LETTER-CHEM-2027"
    qr_path = os.path.join(base_dir, "qr_offer_letter.png")
    qr = qrcode.QRCode(box_size=4, border=1)
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="#800000", back_color="white")
    qr_img.save(qr_path)

    # Document setup: A4 (595.27 x 841.89 pt) with 38pt margins -> 519.27 pt width
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=38,
        rightMargin=38,
        topMargin=32,
        bottomMargin=30,
    )

    styles = getSampleStyleSheet()

    # Shared Brand Colors
    primary_maroon = colors.HexColor('#800000')
    charcoal = colors.HexColor('#1a1a1a')
    slate_gray = colors.HexColor('#4a5568')
    border_gray = colors.HexColor('#d1d5db')
    bg_light = colors.HexColor('#fcf9f9')
    divider_sandstone = colors.HexColor('#b5aea7')

    # Typography Styles - Uniform across all pages
    header_right_style = ParagraphStyle(
        'HeaderRightCommon',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=11.2,
        textColor=charcoal,
    )

    p_body_style = ParagraphStyle(
        'DocBodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.85,
        leading=12.7,
        textColor=charcoal,
        alignment=4, # Justified
        spaceAfter=7,
    )

    section_heading = ParagraphStyle(
        'SectionHeadingCommon',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.0,
        leading=12.2,
        textColor=primary_maroon,
        spaceBefore=6,
        spaceAfter=3,
    )

    small_text = ParagraphStyle(
        'SmallNoticeCommon',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.2,
        leading=9.5,
        textColor=slate_gray,
    )

    def make_uchicago_header(department_markup):
        """Creates the official UChicago letterhead matching Page 1 exactly."""
        if os.path.exists(logo_path):
            logo_img = RLImage(logo_path, width=185, height=39.5)
        else:
            logo_img = Paragraph("<b>THE UNIVERSITY OF CHICAGO</b>", styles['Normal'])

        right_p = Paragraph(department_markup, header_right_style)
        hdr_table = Table([[logo_img, right_p]], colWidths=[310, 209])
        hdr_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (0, 0), 0),
            ('RIGHTPADDING', (0, 0), (0, 0), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ('LEFTPADDING', (1, 0), (1, 0), 14),
            ('LINEBEFORE', (1, 0), (1, 0), 1.2, divider_sandstone),
        ]))
        return hdr_table

    def make_uchicago_footer(unit_name, doc_title, page_num):
        """Creates the official UChicago footer matching Page 1 exactly."""
        footer_tbl = Table([[
            Paragraph(f"<font color='#800000'><b>THE UNIVERSITY OF CHICAGO</b></font> • {unit_name} • {doc_title}", small_text),
            Paragraph(f"Page {page_num} of 3", ParagraphStyle(f'FooterP{page_num}', parent=small_text, alignment=2))
        ]], colWidths=[420, 99])
        footer_tbl.setStyle(TableStyle([
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('LINEABOVE', (0, 0), (-1, -1), 0.5, primary_maroon),
        ]))
        return footer_tbl

    elements = []

    # =========================================================================
    # PAGE 1: OFFICIAL LETTER FROM DEAN JAMES G. NONDORF
    # =========================================================================
    p1_dept_text = (
        "<b><font color='#800000'>Office of College Admissions</font></b><br/><br/>"
        "1101 East 58th Street<br/>"
        "Chicago, IL 60637<br/><br/>"
        "collegeadmissions@uchicago.asia<br/>"
        "T: 773.702.8650<br/>"
        "F: 773.702.4199"
    )
    elements.append(make_uchicago_header(p1_dept_text))
    elements.append(Spacer(1, 22))

    # Date
    p1_date = Paragraph("October 16, 2026", ParagraphStyle('P1Date', parent=styles['Normal'], fontName='Helvetica', fontSize=9.5, leading=13, textColor=charcoal))
    elements.append(p1_date)
    elements.append(Spacer(1, 10))

    # Recipient
    p1_recipient = Paragraph(
        "<b>Devendra Dubey</b><br/>"
        "G-704, Lodha Elite, Lodha Heaven<br/>"
        "Nilje, Maharashtra 421204, India<br/>"
        "<font color='#555555' size='8'>Applicant ID: <b>UC-2027-89321</b> &nbsp;|&nbsp; UCID: <b>12489321</b></font>",
        ParagraphStyle('P1Recip', parent=styles['Normal'], fontName='Helvetica', fontSize=8.8, leading=12.2, textColor=charcoal)
    )
    elements.append(p1_recipient)
    elements.append(Spacer(1, 12))

    # Salutation
    elements.append(Paragraph("<b>Dear Devendra Dubey,</b>", ParagraphStyle('P1Salute', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.5, leading=13, textColor=charcoal)))
    elements.append(Spacer(1, 7))

    # Body Paragraphs
    let_p1 = (
        "On behalf of the faculty, the Admissions Committee, and the entire academic community of <b>The University of Chicago</b>, "
        "it is my absolute pleasure and distinct honor to offer you admission to the <b>Doctor of Philosophy (Ph.D.) degree program "
        "in Chemistry</b> beginning in the <b>Autumn Quarter 2027</b>."
    )
    elements.append(Paragraph(let_p1, p_body_style))

    let_p2 = (
        "Admission to the University of Chicago is among the most competitive in the world, extended only to scholars of uncommon "
        "intellect, purpose, and originality. Among thousands of exceptional candidates from across the globe, your dossier stood "
        "out for its profound scientific maturity and rigorous analytical capability. The admissions committee was deeply impressed "
        "by your academic record at the <b>Indian Institute of Technology Gandhinagar (IITGN)</b>, your first-class honors, and the "
        "stellar commendations provided by your faculty referees."
    )
    elements.append(Paragraph(let_p2, p_body_style))

    let_p3 = (
        "In particular, our faculty selection panel and <b>Professor Alex (Alexander Q.) Cusumano</b> conducted an exhaustive "
        "review of your research portfolio, specifically commending your <b>editor-led computational research project and software architectures</b>. "
        "Professor Cusumano praised the technical elegance, algorithmic depth, and creative execution demonstrated throughout your work. "
        "Reflecting this high praise, <b>Professor Alex Cusumano has officially accepted you into the Cusumano Research Group in the Searle "
        "Chemistry Laboratories</b> as your designated Faculty Research Advisor."
    )
    elements.append(Paragraph(let_p3, p_body_style))

    let_p4 = (
        "At Chicago, we are committed to ensuring that every doctoral scholar is fully supported throughout their scholarly journey. "
        "I am delighted to confirm that you have been awarded a <b>100% fully funded doctoral fellowship package</b>, guaranteeing full "
        "tuition remission ($20,000 per semester), complete individual U-SHIP health coverage, and an annual living stipend of $36,000 "
        "($3,000 per month). Comprehensive details of your fellowship, departmental placement, and seat locking guarantee are detailed "
        "in the enclosed departmental dossier."
    )
    elements.append(Paragraph(let_p4, p_body_style))

    let_p5 = (
        "UChicago is an environment where foundational questions are asked and transformative ideas are born. We know that your "
        "scholarly voice and drive will make lasting contributions to our university and the field of chemical sciences. "
        "Please accept our warmest congratulations and our enthusiastic welcome to Hyde Park."
    )
    elements.append(Paragraph(let_p5, p_body_style))
    elements.append(Spacer(1, 8))

    # Sign-off & Signature
    elements.append(Paragraph("Kind regards,", ParagraphStyle('P1Close', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=12, textColor=charcoal)))
    elements.append(Spacer(1, 4))

    if os.path.exists(sig_dean_path):
        sig_img = RLImage(sig_dean_path, width=96, height=50)
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
    elements.append(make_uchicago_footer("Office of College Admissions", "Official Letter of Admission", 1))

    # =========================================================================
    # PAGE 2: DEPARTMENT OF CHEMISTRY • FACULTY SPONSORSHIP & RESEARCH PLACEMENT
    # =========================================================================
    elements.append(PageBreak())

    p2_dept_text = (
        "<b><font color='#800000'>Department of Chemistry</font></b><br/><br/>"
        "Division of the Physical Sciences<br/>"
        "Searle Chemistry Laboratories<br/>"
        "5735 S. Ellis Avenue, Chicago, IL 60637<br/><br/>"
        "chem-admissions@uchicago.asia<br/>"
        "T: 773.702.7250<br/>"
        "F: 773.702.0805"
    )
    elements.append(make_uchicago_header(p2_dept_text))
    elements.append(Spacer(1, 20))

    # Date & Dossier Identification Block
    p2_date = Paragraph("October 16, 2026", ParagraphStyle('P2Date', parent=styles['Normal'], fontName='Helvetica', fontSize=9.5, leading=13, textColor=charcoal))
    elements.append(p2_date)
    elements.append(Spacer(1, 10))

    p2_dossier_hdr = Paragraph(
        "<b>FACULTY SPONSORSHIP &amp; LABORATORY PLACEMENT DOSSIER</b><br/>"
        "Candidate: <b>Devendra Dubey</b> &nbsp;|&nbsp; Degree: <b>Ph.D. in Chemistry</b> &nbsp;|&nbsp; Term: <b>Autumn Quarter 2027</b><br/>"
        "<font color='#555555' size='8'>Applicant ID: <b>UC-2027-89321</b> &nbsp;|&nbsp; UCID: <b>12489321</b> &nbsp;|&nbsp; Ref: <b>UCHI-PSD-CHEM-OFFER-2027-89321</b></font>",
        ParagraphStyle('P2DossierHdr', parent=styles['Normal'], fontName='Helvetica', fontSize=8.8, leading=12.2, textColor=charcoal)
    )
    elements.append(p2_dossier_hdr)
    elements.append(Spacer(1, 12))

    # Salutation
    elements.append(Paragraph("<b>Dear Devendra,</b>", ParagraphStyle('P2Salute', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.5, leading=13, textColor=charcoal)))
    elements.append(Spacer(1, 7))

    # Narrative Body
    p2_b1 = (
        "On behalf of the Graduate Faculty of the Department of Chemistry and the Division of the Physical Sciences at "
        "<b>The University of Chicago</b>, I am delighted to welcome you to our department. Following your official university "
        "admission by Dean James G. Nondorf, this departmental communication confirms your formal faculty sponsorship, "
        "laboratory assignment, and doctoral research placement beginning in the <b>Autumn Quarter 2027</b>."
    )
    elements.append(Paragraph(p2_b1, p_body_style))

    p2_b2 = (
        "Admission to doctoral study in the Department of Chemistry is granted only to individuals demonstrating extraordinary "
        "intellectual independence, analytical rigor, and research potential. Your master's achievements at the <b>Indian Institute "
        "of Technology Gandhinagar (IITGN)</b>, distinguished by first-class honors and highest commendations from your faculty "
        "referees, placed your application at the very forefront of our international admissions pool."
    )
    elements.append(Paragraph(p2_b2, p_body_style))

    # Elegant Executive Commendation Callout (Matches UChicago clean aesthetic)
    commend_markup = (
        "<b><font color='#800000'>FACULTY COMMENDATION &amp; LABORATORY ACCEPTANCE</font></b><br/><br/>"
        "The Admissions Committee and Faculty Selection Panel conducted a comprehensive evaluation of your research portfolio, "
        "specifically reviewing your <b>editor-led computational research project and software architectures</b>. "
        "<b>Professor Alex (Alexander Q.) Cusumano</b>, Assistant Professor of Chemistry (Computational &amp; Theoretical Chemistry, "
        "Molecular Dynamics, Catalysis), was extraordinarily impressed by the technical depth, algorithmic rigor, and creative "
        "methodological execution demonstrated across your editor-led project.<br/><br/>"
        "Reflecting this exceptional commendation, <b>Professor Alex Cusumano has officially accepted you into the Cusumano Research "
        "Group in the Searle Chemistry Laboratories as your designated Faculty Research Advisor</b>. Both Professor Cusumano and "
        "our faculty look forward to mentoring you as you advance groundbreaking investigations in computational chemistry and "
        "reaction catalysis."
    )
    commend_table = Table([[Paragraph(commend_markup, ParagraphStyle('CommendTxt', parent=styles['Normal'], fontName='Helvetica', fontSize=8.4, leading=12.2, textColor=charcoal))]], colWidths=[519])
    commend_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg_light),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
        ('LINEBEFORE', (0, 0), (0, -1), 2.5, primary_maroon),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#e8dfdf')),
    ]))
    elements.append(commend_table)
    elements.append(Spacer(1, 10))

    # Formal Research Placement Specifications (Clean, minimal hairline table)
    placement_specs = [
        [
            Paragraph("<b>Faculty Research Advisor:</b>", ParagraphStyle('PL1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, textColor=primary_maroon)),
            Paragraph("Prof. Alex (Alexander Q.) Cusumano, Ph.D. — Assistant Professor of Chemistry", ParagraphStyle('PL2', parent=styles['Normal'], fontName='Helvetica', fontSize=8.2, textColor=charcoal))
        ],
        [
            Paragraph("<b>Designated Research Group:</b>", ParagraphStyle('PL1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, textColor=primary_maroon)),
            Paragraph("The Cusumano Research Group • Computational &amp; Theoretical Chemistry Laboratory", ParagraphStyle('PL2', parent=styles['Normal'], fontName='Helvetica', fontSize=8.2, textColor=charcoal))
        ],
        [
            Paragraph("<b>Primary Laboratory Facility:</b>", ParagraphStyle('PL1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, textColor=primary_maroon)),
            Paragraph("Searle Chemistry Laboratories, Suite 214–220, 5735 S. Ellis Ave, Chicago, IL 60637", ParagraphStyle('PL2', parent=styles['Normal'], fontName='Helvetica', fontSize=8.2, textColor=charcoal))
        ],
        [
            Paragraph("<b>Doctoral Research Focus:</b>", ParagraphStyle('PL1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, textColor=primary_maroon)),
            Paragraph("Computational Catalysis, Molecular Dynamics Simulations &amp; Algorithmic Chemical Modeling", ParagraphStyle('PL2', parent=styles['Normal'], fontName='Helvetica', fontSize=8.2, textColor=charcoal))
        ]
    ]
    pl_table = Table(placement_specs, colWidths=[150, 369])
    pl_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#fdfcfc')),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor('#eaeaea')),
        ('BOX', (0, 0), (-1, -1), 0.5, border_gray),
    ]))
    elements.append(pl_table)
    elements.append(Spacer(1, 12))

    # Official Departmental Endorsement Record on Page 2
    elements.append(Spacer(1, 8))
    p2_cert_text = (
        "<b>OFFICIAL DEPARTMENTAL ENDORSEMENT &amp; FACULTY PLACEMENT RECORD</b><br/>"
        "This laboratory placement and faculty sponsorship dossier has been formally approved and certified by the "
        "Department of Chemistry Graduate Admissions Committee and the Cusumano Research Group. All supervisory allocations, "
        "computational laboratory resources, and doctoral workspace provisions are formally ratified and incorporated into the "
        "institutional admission credential issued under the authority of Dean James G. Nondorf."
    )
    p2_cert_table = Table([[
        Paragraph(p2_cert_text, ParagraphStyle('P2Cert', parent=styles['Normal'], fontName='Helvetica', fontSize=8.0, leading=11.2, textColor=charcoal))
    ]], colWidths=[519])
    p2_cert_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#faf7f7')),
        ('BOX', (0, 0), (-1, -1), 0.5, border_gray),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('LINEBEFORE', (0, 0), (0, -1), 2.2, primary_maroon),
    ]))
    elements.append(p2_cert_table)

    # Page 2 Footer
    elements.append(Spacer(1, 14))
    elements.append(make_uchicago_footer("Department of Chemistry", "Faculty Sponsorship & Research Placement", 2))

    # =========================================================================
    # PAGE 3: FELLOWSHIP AWARD, TUITION, STIPEND, DEPOSIT TERMS & RATIFICATION
    # =========================================================================
    elements.append(PageBreak())

    p3_dept_text = (
        "<b><font color='#800000'>Division of the Physical Sciences</font></b><br/><br/>"
        "Office of Graduate Education &amp; Fellowships<br/>"
        "Eckhardt Research Center, Suite 208<br/>"
        "5640 S. Ellis Avenue, Chicago, IL 60637<br/><br/>"
        "psd-fellowships@uchicago.asia<br/>"
        "T: 773.702.7950<br/>"
        "F: 773.702.8526"
    )
    elements.append(make_uchicago_header(p3_dept_text))
    elements.append(Spacer(1, 10))

    # Date & Dossier Identification Block
    p3_date = Paragraph("October 16, 2026", ParagraphStyle('P3Date', parent=styles['Normal'], fontName='Helvetica', fontSize=9.5, leading=13, textColor=charcoal))
    elements.append(p3_date)
    elements.append(Spacer(1, 6))

    p3_dossier_hdr = Paragraph(
        "<b>DOCTORAL FELLOWSHIP AWARD &amp; ENROLLMENT RATIFICATION</b><br/>"
        "Candidate: <b>Devendra Dubey</b> &nbsp;|&nbsp; Degree: <b>Ph.D. in Chemistry</b> &nbsp;|&nbsp; Matriculation: <b>Autumn Quarter 2027</b><br/>"
        "<font color='#555555' size='8'>Applicant ID: <b>UC-2027-89321</b> &nbsp;|&nbsp; UCID: <b>12489321</b> &nbsp;|&nbsp; Institutional Award Ref: <b>UCHI-PSD-CHEM-OFFER-2027-89321</b></font>",
        ParagraphStyle('P3DossierHdr', parent=styles['Normal'], fontName='Helvetica', fontSize=8.8, leading=12.2, textColor=charcoal)
    )
    elements.append(p3_dossier_hdr)
    elements.append(Spacer(1, 6))

    # Intro narrative
    p3_intro = (
        "The University of Chicago is steadfastly committed to ensuring that every doctoral scholar is fully supported. "
        "Throughout your graduate tenure in good academic standing, you are awarded an institutionally guaranteed "
        "fellowship package covering your complete tuition, mandatory health insurance, and annual living expenses:"
    )
    elements.append(Paragraph(p3_intro, p_body_style))
    elements.append(Spacer(1, 3))

    # Financial Breakdown Table - Refined, executive academic styling
    fin_data = [
        [
            Paragraph("<b><font color='#800000'>AWARD COMPONENT</font></b>", ParagraphStyle('FH1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.5, leading=10)),
            Paragraph("<b><font color='#800000'>GUARANTEED VALUE</font></b>", ParagraphStyle('FH2', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.5, leading=10)),
            Paragraph("<b><font color='#800000'>DISBURSEMENT &amp; COVERAGE TERMS</font></b>", ParagraphStyle('FH3', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.5, leading=10))
        ],
        [
            Paragraph("<b>Full Tuition Remission</b>", ParagraphStyle('FD1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, textColor=charcoal)),
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
            Paragraph("<b>$6,200.00 USD</b><br/><font color='#800000' size='7'><b>Due: November 14, 2026</b></font>", ParagraphStyle('FD2', parent=styles['Normal'], fontName='Helvetica', fontSize=8, textColor=charcoal)),
            Paragraph("<b>Reimbursable/refundable ONLY in case of non-admission</b> (e.g., visa denial or cancellation). Mandatory upon enrollment.", ParagraphStyle('FD3', parent=styles['Normal'], fontName='Helvetica', fontSize=8, textColor=primary_maroon))
        ]
    ]
    fin_table = Table(fin_data, colWidths=[132, 122, 265])
    fin_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#faf4f4')),
        ('LINEBELOW', (0, 0), (-1, 0), 1.0, primary_maroon),
        ('LINEABOVE', (0, 0), (-1, 0), 0.5, border_gray),
        ('BOX', (0, 0), (-1, -1), 0.5, border_gray),
        ('INNERGRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#f0ecec')),
        ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#ffffff')),
        ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#fdfcfc')),
        ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor('#ffffff')),
        ('BACKGROUND', (0, 4), (-1, 4), colors.HexColor('#fdf9f9')),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    elements.append(fin_table)
    elements.append(Spacer(1, 6))

    # Terms of Seat Locking Deposit
    elements.append(Paragraph("<b>TERMS OF SEAT CONFIRMATION DEPOSIT &amp; GUARANTEED REFUND POLICY</b>", section_heading))
    p_deposit_terms = (
        "To reserve and officially lock your graduate research placement in the Cusumano Laboratory, admitted candidates submit a "
        "Ph.D. Matriculation Seat Confirmation Deposit of <b>$6,200.00 USD</b> by the priority deadline of <b>November 14, 2026</b>. "
        "The University maintains the following strict institutional guarantee governing this deposit:<br/>"
        "• <b>Reimbursement &amp; Refund Policy (Non-Admission Only):</b> The $6,200.00 USD seat locking fee is <b>100% reimbursable or refundable "
        "ONLY in case of non-admission</b> (such as in the event of unforeseen visa refusal/denial, international travel restrictions, or administrative "
        "cancellation prior to matriculation), payable within 90 business days upon submission of written notification and supporting documentation "
        "to the Division of the Physical Sciences Admissions Office.<br/>"
        "• <b>Mandatory Institutional Fee Upon Enrollment:</b> In all other cases upon formal admission and program matriculation, the deposit is "
        "mandatory, credited towards student bursar account and research placement lock, and is <b>strictly non-reimbursable and non-refundable</b>."
    )
    elements.append(Paragraph(p_deposit_terms, p_body_style))
    elements.append(Spacer(1, 4))

    # Acceptance Instructions & Next Steps
    elements.append(Paragraph("<b>ENROLLMENT CONFIRMATION &amp; VISA ISSUANCE</b>", section_heading))
    p_next_steps = (
        "Please confirm your doctoral matriculation by logging in to your secure <b>Applicant Status Portal</b> at "
        "<b>https://uchicago.asia/portal.html?applicantId=UC-2027-89321</b>. Upon receipt of your enrollment response and seat deposit, "
        "the Office of International Affairs (OIA) will immediately issue your Form I-20 Certificate of Eligibility for Nonimmigrant "
        "Student Status (F-1 visa processing)."
    )
    elements.append(Paragraph(p_next_steps, p_body_style))
    elements.append(Spacer(1, 5))

    # Ratification & Signatures Block on Page 3
    sig_content = []
    
    # Col 1: Dean James G. Nondorf Signature
    col1 = []
    col1.append(Paragraph("Sincerely,", ParagraphStyle('P3Close', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11, textColor=charcoal)))
    col1.append(Spacer(1, 2))
    if os.path.exists(sig_dean_path):
        sig_dean_p3 = RLImage(sig_dean_path, width=76, height=42)
        sig_dean_p3.hAlign = 'LEFT'
        col1.append(sig_dean_p3)
        col1.append(Spacer(1, 2))
    col1.append(Paragraph(
        "<b>James G. Nondorf</b><br/>"
        "Dean of Admissions and Financial Aid<br/>"
        "Vice President for Enrollment<br/>"
        "The University of Chicago",
        ParagraphStyle('S3', parent=styles['Normal'], fontName='Helvetica', fontSize=7.8, leading=10.2, textColor=charcoal)
    ))

    # Col 2: Institutional Seal & Official Ratification
    col2 = []
    seal_table_data = []
    if os.path.exists(shield_path):
        seal_img = RLImage(shield_path, width=32, height=34)
    else:
        seal_img = Paragraph("SEAL", styles['Normal'])
    seal_txt = Paragraph(
        "<b>OFFICIAL INSTITUTIONAL SEAL</b><br/>"
        "Division of the Physical Sciences<br/>"
        "<font size='6.5' color='#555'>Document Hash: 89321-PSD-CHEM-SHA256<br/>"
        "Digitally Signed, Sealed &amp; Ratified</font>",
        ParagraphStyle('SealTxt', parent=styles['Normal'], fontName='Helvetica', fontSize=7.2, leading=9.5, textColor=charcoal)
    )
    col2.append(Table([[seal_img, seal_txt]], colWidths=[38, 140]))

    # Col 3: QR Code
    col3 = []
    if os.path.exists(qr_path):
        qr_obj = RLImage(qr_path, width=44, height=44)
    else:
        qr_obj = Paragraph("QR", styles['Normal'])
    qr_txt = Paragraph(
        "<font size='6.5' color='#555'><b>Secure Verification</b><br/>uchicago.asia/portal<br/>Scan to Authenticate</font>",
        ParagraphStyle('QRTxt', parent=styles['Normal'], fontName='Helvetica', fontSize=6.5, leading=8.5, textColor=charcoal, alignment=1)
    )
    col3.append(qr_obj)
    col3.append(qr_txt)

    sig_ratification_table = Table([[col1, col2, col3]], colWidths=[200, 209, 110])
    sig_ratification_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, border_gray),
    ]))
    elements.append(sig_ratification_table)

    # Page 3 Footer
    elements.append(Spacer(1, 6))
    elements.append(make_uchicago_footer("Division of the Physical Sciences", "Fellowship Award & Enrollment Terms", 3))

    # Build the PDF
    doc.build(elements)
    print(f"Generated Official Offer Letter PDF at {pdf_path}")

    # Render high-resolution PNG previews using PyMuPDF
    pdf_doc = pymupdf.open(pdf_path)
    total_pages = len(pdf_doc)
    print(f"Total Pages in generated PDF: {total_pages}")
    
    p1 = pdf_doc[0]
    pix1 = p1.get_pixmap(dpi=144)
    pix1.save(img_page1)
    print(f"Rendered Page 1 PNG preview at {img_page1} ({pix1.width}x{pix1.height})")

    if total_pages > 1:
        p2 = pdf_doc[1]
        pix2 = p2.get_pixmap(dpi=144)
        pix2.save(img_page2)
        print(f"Rendered Page 2 PNG preview at {img_page2} ({pix2.width}x{pix2.height})")

    if total_pages > 2:
        p3 = pdf_doc[2]
        pix3 = p3.get_pixmap(dpi=144)
        pix3.save(img_page3)
        print(f"Rendered Page 3 PNG preview at {img_page3} ({pix3.width}x{pix3.height})")

if __name__ == "__main__":
    build_pdf_offer_letter()
    print("Offer letter built successfully!")
