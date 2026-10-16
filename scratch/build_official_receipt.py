import os
import qrcode
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, KeepTogether, HRFlowable
)
import pymupdf

def generate_receipt():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    site_dir = os.path.join(base_dir, "..", "site_1to1")
    doc_dir = os.path.join(site_dir, "assets", "documents")
    os.makedirs(doc_dir, exist_ok=True)
    pdf_path = os.path.join(doc_dir, "Official_Receipt_UCHI_2027_6200.pdf")
    img_path = os.path.join(doc_dir, "receipt_page_1.png")

    # Generate QR Code image
    qr_path = os.path.join(base_dir, "receipt_qr.png")
    qr = qrcode.QRCode(box_size=4, border=1)
    qr.add_data("https://uchicago.asia/portal.html?txId=TXN-UCHI-2026-89321&ref=REF-UCHI-DEP-2027-6200")
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="#1a1a1a", back_color="white")
    qr_img.save(qr_path)

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=32,
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.HexColor('#800000'),
        alignment=0,
    )

    sub_title_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#555555'),
        alignment=0,
    )

    h_univ = ParagraphStyle(
        'UnivHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=16,
        textColor=colors.HexColor('#800000'),
    )

    h_sub = ParagraphStyle(
        'UnivSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#444444'),
    )

    cell_bold = ParagraphStyle(
        'CellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#111111'),
    )

    cell_norm = ParagraphStyle(
        'CellNorm',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#333333'),
    )

    cell_label = ParagraphStyle(
        'CellLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#666666'),
    )

    cell_val = ParagraphStyle(
        'CellVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#111111'),
    )

    notice_style = ParagraphStyle(
        'Notice',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#555555'),
        alignment=1,
    )

    elements = []

    # 1. Top Decorative Bar
    elements.append(HRFlowable(width="100%", thickness=4, color=colors.HexColor('#800000'), spaceAfter=10))

    # 2. Header Table: University branding & Crest info
    header_data = [
        [
            Paragraph("<strong>THE UNIVERSITY OF CHICAGO</strong><br/><font color='#666666' size='8'>Office of the Bursar &amp; Student Accounts • Division of the Physical Sciences<br/>Searle Chemistry Laboratories • 5801 S. Ellis Avenue, Chicago, IL 60637 USA</font>", h_univ),
            Paragraph("<font color='#800000'><strong>OFFICIAL INSTITUTIONAL RECEIPT</strong></font><br/><font color='#555555' size='8'>Tax Year: 2026–2027 • Form 1098-T Eligible<br/>Reference: <strong>REF-UCHI-DEP-2027-6200</strong></font>", ParagraphStyle('HRight', parent=h_sub, alignment=2))
        ]
    ]
    header_table = Table(header_data, colWidths=[330, 193])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    elements.append(header_table)
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#dddddd'), spaceAfter=8))

    # 3. Document Title
    elements.append(Paragraph("OFFICIAL STUDENT ACCOUNTS TAX RECEIPT &amp; ENROLLMENT MANDATE", title_style))
    elements.append(Paragraph("Graduate Matriculation Deposit • Computational Chemistry Doctoral Program (Autumn 2027)", sub_title_style))
    elements.append(Spacer(1, 10))

    # 4. Two-Column Metadata Summary Box
    summary_data = [
        [
            Paragraph("<strong>TRANSACTION IDENTIFIERS</strong>", cell_bold),
            Paragraph("<strong>SETTLEMENT &amp; PROGRAM DATES</strong>", cell_bold)
        ],
        [
            Paragraph("<strong>Transaction ID:</strong> TXN-UCHI-2026-89321<br/>"
                      "<strong>Invoice Number:</strong> INV-UCHI-2026-89321<br/>"
                      "<strong>Bank Approval Code:</strong> AUTH-UCHI-89321<br/>"
                      "<strong>Account Reference:</strong> REF-UCHI-DEP-2027-6200<br/>"
                      "<strong>Issuing Channel:</strong> Bursar Direct Mandate Clearing", cell_norm),
            Paragraph("<strong>Settlement Status:</strong> <font color='#137333'><strong>CONFIRMED &amp; SETTLED (PAID)</strong></font><br/>"
                      "<strong>Transaction Date:</strong> 16 October 2026, 03:00:00 IST<br/>"
                      "<strong>Seat Locking Priority Deadline:</strong> Nov 15, 2026<br/>"
                      "<strong>Doctoral Matriculation:</strong> August 2027<br/>"
                      "<strong>Autumn Quarter Classes:</strong> September 2027", cell_norm)
        ]
    ]
    summary_table = Table(summary_data, colWidths=[260, 263])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f8f4f4')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#ffffff')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#d9c5c5')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#eeeeee')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    elements.append(summary_table)
    elements.append(Spacer(1, 10))

    # 5. Candidate / Student & Billing Profile Table
    student_data = [
        [
            Paragraph("<strong>CANDIDATE / STUDENT INFORMATION</strong>", cell_bold),
            Paragraph("<strong>BILLING &amp; REMITTANCE ADDRESS</strong>", cell_bold)
        ],
        [
            Paragraph("<strong>Candidate Name:</strong> Devendra Dubey<br/>"
                      "<strong>Student Full Name:</strong> Devendra Dubey Biswambharnath Geeta<br/>"
                      "<strong>Applicant Portal ID:</strong> UC-2027-89321<br/>"
                      "<strong>Student ID (UCID):</strong> 12489321<br/>"
                      "<strong>Notification Email:</strong> devendra.dubey@iitgn.ac.in<br/>"
                      "<strong>Academic Unit:</strong> Division of the Physical Sciences<br/>"
                      "<strong>Degree Program:</strong> Doctor of Philosophy (Ph.D.) in Chemistry<br/>"
                      "<strong>Faculty Advisor:</strong> Prof. Alex (Alexander Q.) Cusumano", cell_norm),
            Paragraph("<strong>Billing Contact:</strong> Devendra Dubey<br/>"
                      "<strong>Relationship:</strong> Self - Doctoral Candidate<br/>"
                      "<strong>Address Line 1:</strong> G-704, Lodha Elite<br/>"
                      "<strong>Address Line 2:</strong> Lodha Heaven<br/>"
                      "<strong>City / State:</strong> Nilje, Maharashtra<br/>"
                      "<strong>Postal Code:</strong> 421204<br/>"
                      "<strong>Country:</strong> India<br/>"
                      "<strong>Bursar Remittance:</strong> Wire/Electronic Mandate Settlement", cell_norm)
        ]
    ]
    student_table = Table(student_data, colWidths=[260, 263])
    student_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f8f4f4')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#ffffff')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#d9c5c5')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#eeeeee')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    elements.append(student_table)
    elements.append(Spacer(1, 10))

    # 6. Itemized Fee Schedule
    items_header = [
        Paragraph("<strong>ITEM CODE</strong>", cell_bold),
        Paragraph("<strong>DESCRIPTION &amp; DESIGNATION</strong>", cell_bold),
        Paragraph("<strong>TERM</strong>", cell_bold),
        Paragraph("<strong>AMOUNT (USD)</strong>", ParagraphStyle('RBold', parent=cell_bold, alignment=2)),
    ]
    row_item = [
        Paragraph("<strong>UC-CHEM-PHD-2027</strong>", cell_norm),
        Paragraph("<strong>Ph.D. Matriculation Seat Locking &amp; Enrollment Deposit</strong><br/>"
                  "<font size='7.5' color='#555'>Computational Chemistry Doctoral Program • Cusumano Research Group<br/>"
                  "Searle Chemistry Laboratories • Credited to Student Bursar Account</font>", cell_norm),
        Paragraph("Autumn 2027<br/><font size='7.5' color='#666'>Priority: Nov 15, 2026</font>", cell_norm),
        Paragraph("$6,200.00", ParagraphStyle('RNorm', parent=cell_norm, alignment=2)),
    ]
    row_subtotal = [
        "",
        Paragraph("<strong>Subtotal (Tuition Deposit)</strong>", cell_norm),
        "",
        Paragraph("$6,200.00", ParagraphStyle('RNorm', parent=cell_norm, alignment=2)),
    ]
    row_waiver = [
        "",
        Paragraph("<strong>Departmental Fellowship Remission</strong> (100% Tuition Waiver Applied)", cell_norm),
        "",
        Paragraph("-$0.00", ParagraphStyle('RNorm', parent=cell_norm, alignment=2)),
    ]
    row_tax = [
        "",
        Paragraph("<strong>Sales / Academic Institutional Tax (0.00%)</strong>", cell_norm),
        "",
        Paragraph("$0.00", ParagraphStyle('RNorm', parent=cell_norm, alignment=2)),
    ]
    row_total = [
        "",
        Paragraph("<strong>TOTAL PAID &amp; SETTLED</strong>", cell_bold),
        Paragraph("<strong>PAID IN FULL</strong>", ParagraphStyle('GBold', parent=cell_bold, textColor=colors.HexColor('#137333'))),
        Paragraph("<strong>$6,200.00 USD</strong>", ParagraphStyle('RTotal', parent=cell_bold, alignment=2, textColor=colors.HexColor('#800000'), fontSize=10.5)),
    ]

    items_data = [items_header, row_item, row_subtotal, row_waiver, row_tax, row_total]
    items_table = Table(items_data, colWidths=[110, 245, 88, 80])
    items_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#800000')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cccccc')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#eeeeee')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#ffffff')),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#f8f4f4')),
        ('LINEABOVE', (0,-1), (-1,-1), 1.5, colors.HexColor('#800000')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(items_table)
    elements.append(Spacer(1, 10))

    # 7. Payment Instrument & Mandate Details Table (incorporating exact Discover card details)
    card_info_html = (
        "<strong>Payment Instrument:</strong> Direct Mandate Pre-Authorized Debit Card<br/>"
        "<strong>Card Brand:</strong> Discover Debit Card (Global Partner Direct Clearing)<br/>"
        "<strong>Card Number:</strong> •••• •••• •••• 0405 (Last 4: 0405)<br/>"
        "<strong>Cardholder Name:</strong> Devendra Dubey<br/>"
        "<strong>Expiration Date:</strong> 04/32 • <strong>Security Clearance:</strong> 2FA OTP Verified<br/>"
        "<strong>Mandate Status:</strong> <font color='#137333'><strong>Verified &amp; Pre-Authorized Mandate Active</strong></font><br/>"
        "<strong>Issuing Institution:</strong> Stanford Federal Credit Union / Global Partner Bank<br/>"
        "<strong>Mandate Authorization Reference:</strong> AUTH-STAN-807081 / AUTH-UCHI-89321"
    )

    qr_image = RLImage(qr_path, width=70, height=70)

    auth_data = [
        [
            Paragraph("<strong>PRE-AUTHORIZED PAYMENT INSTRUMENT &amp; MANDATE CLEARING</strong>", cell_bold),
            Paragraph("<strong>INSTITUTIONAL VALIDATION</strong>", cell_bold)
        ],
        [
            Paragraph(card_info_html, cell_norm),
            Table([
                [qr_image, Paragraph("<font size='7' color='#444'><strong>OFFICIAL DIGITAL SEAL</strong><br/>Scan QR code to verify bursar payment settlement on file with UChicago Student Financial Services.<br/><strong>Status: SETTLED</strong></font>", cell_norm)]
            ], colWidths=[74, 96], style=[
                ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                ('LEFTPADDING', (0,0), (-1,-1), 0),
                ('RIGHTPADDING', (0,0), (-1,-1), 0),
                ('TOPPADDING', (0,0), (-1,-1), 0),
                ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ])
        ]
    ]

    auth_table = Table(auth_data, colWidths=[340, 183])
    auth_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f8f4f4')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#ffffff')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#d9c5c5')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#eeeeee')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    elements.append(auth_table)
    elements.append(Spacer(1, 10))

    # 8. Legal Notice & Signatures
    notice_text = (
        "<strong>Official Tax Receipt &amp; Payment Mandate Confirmation</strong> issued under University of Chicago Student Accounts. "
        "Retain this official institutional receipt for your academic records, corporate or fellowship tuition reimbursement, and IRS/tax reporting purposes. "
        "The seat reservation deposit guarantees matriculation placement in the doctoral research program under Prof. Alex Cusumano for Autumn 2027. "
        "Inquiries: Office of the Bursar, bursar@uchicago.asia • Phone: +1 (773) 702-8000 • 5801 S. Ellis Ave, Chicago, IL 60637."
    )
    elements.append(Paragraph(notice_text, notice_style))
    elements.append(Spacer(1, 6))

    sig_data = [
        [
            Paragraph("<strong>Brett A. Bennett</strong><br/><font size='7.5' color='#666'>University Bursar &amp; Comptroller<br/>The University of Chicago</font>", cell_norm),
            Paragraph("<strong>Prof. Viresh Rawal</strong><br/><font size='7.5' color='#666'>Chairman, Department of Chemistry<br/>Division of the Physical Sciences</font>", cell_norm),
            Paragraph("<font color='#137333'><strong>DIGITALLY CLEARED</strong></font><br/><font size='7.5' color='#666'>Automated Clearing House (ACH/Debit)<br/>Ref #UCHI-DEP-2027-6200</font>", cell_norm),
        ]
    ]
    sig_table = Table(sig_data, colWidths=[174, 174, 175])
    sig_table.setStyle(TableStyle([
        ('LINEABOVE', (0,0), (-1,-1), 0.5, colors.HexColor('#cccccc')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    elements.append(sig_table)

    # Build PDF
    doc.build(elements)
    print(f"Generated PDF at {pdf_path}")

    # Render PNG using pymupdf
    pdf_doc = pymupdf.open(pdf_path)
    page = pdf_doc.load_page(0)
    pix = page.get_pixmap(dpi=144)
    pix.save(img_path)
    print(f"Rendered PNG at {img_path} ({pix.width}x{pix.height})")

if __name__ == "__main__":
    generate_receipt()
