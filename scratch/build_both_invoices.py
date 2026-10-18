import os
import qrcode
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, KeepTogether, HRFlowable
)
import pymupdf

def build_pdf_invoice(invoice_type="seat_deposit"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    site_dir = os.path.join(base_dir, "..", "site_1to1")
    doc_dir = os.path.join(site_dir, "assets", "documents")
    os.makedirs(doc_dir, exist_ok=True)

    logo_path = os.path.join(site_dir, "assets", "uchicago_full_logo.png")

    if invoice_type == "seat_deposit":
        pdf_path = os.path.join(doc_dir, "Official_Receipt_UCHI_2027_6200.pdf")
        img_path = os.path.join(doc_dir, "receipt_page_1.png")
        qr_data = "https://uchicago.asia/portal.html?txId=TXN-UCHI-2026-89321&ref=REF-UCHI-DEP-2027-6200&amount=6200"
        doc_title = "OFFICIAL STUDENT ACCOUNTS TAX RECEIPT & ENROLLMENT MANDATE"
        doc_subtitle = "Graduate Matriculation Deposit • Computational Chemistry Doctoral Program (Autumn 2027)"
        ref_num = "REF-UCHI-DEP-2027-6200"
        txn_id = "TXN-UCHI-2026-89321"
        inv_id = "INV-UCHI-2026-89321"
        auth_code = "AUTH-UCHI-89321"
        txn_date = "16 October 2026, 03:00:00 IST"
        secondary_date_label = "Seat Locking Priority Deadline:"
        secondary_date_val = "Nov 15, 2026"
        item_code = "UC-CHEM-PHD-2027"
        item_desc = "<strong>Ph.D. Matriculation Seat Locking &amp; Enrollment Deposit</strong><br/><font color='#555555' size='7.5'>Computational Chemistry Doctoral Program • Cusumano Research Group<br/>Searle Chemistry Laboratories • Credited to Student Bursar Account</font>"
        item_term = "Autumn 2027<br/><font color='#777777' size='7'>Priority: Nov 15, 2026</font>"
        item_amt = "$6,200.00"
        total_amt = "$6,200.00 USD"
        amount_words = "Six Thousand Two Hundred US Dollars and Zero Cents"
        payment_desc = "Debit Card (Direct Mandate Pre-Authorized) - Discover Debit Card (•••• 0405)"
    else: # Application fee invoice
        pdf_path = os.path.join(doc_dir, "Official_Application_Fee_Receipt_UCHI_2026.pdf")
        img_path = os.path.join(doc_dir, "app_fee_receipt_page_1.png")
        qr_data = "https://uchicago.asia/portal.html?txId=TXN-UCHI-APP-2026-100101&ref=REF-UCHI-APP-2026-90&amount=90"
        doc_title = "OFFICIAL GRADUATE ADMISSIONS APPLICATION FEE RECEIPT"
        doc_subtitle = "Doctoral Admissions Application & Dossier Processing Fee • Autumn Quarter 2027"
        ref_num = "REF-UCHI-APP-2026-90"
        txn_id = "TXN-UCHI-APP-2026-100101"
        inv_id = "INV-UCHI-APP-2026-100101"
        auth_code = "AUTH-UCHI-APP-100101"
        txn_date = "1st October 2026, 06:30:00 AM IST"
        secondary_date_label = "Application Filing Term:"
        secondary_date_val = "Autumn Quarter 2027"
        item_code = "UC-GRAD-APP-2027"
        item_desc = "<strong>Graduate Application &amp; Dossier Evaluation Fee</strong><br/><font color='#555555' size='7.5'>Doctor of Philosophy (Ph.D.) in Chemistry — Physical Sciences Division<br/>Electronic Application Processing &amp; Transcripts Verification Fee</font>"
        item_term = "Autumn 2027<br/><font color='#777777' size='7'>Filed: 01 Oct 2026</font>"
        item_amt = "$90.00"
        total_amt = "$90.00 USD"
        amount_words = "Ninety US Dollars and Zero Cents"
        payment_desc = "Debit Card (Direct Mandate Pre-Authorized) - Discover Debit Card (•••• 0405)"

    # Generate QR Code image
    qr_path = os.path.join(base_dir, f"qr_{invoice_type}.png")
    qr = qrcode.QRCode(box_size=4, border=1)
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="#1a1a1a", back_color="white")
    qr_img.save(qr_path)

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=28,
        bottomMargin=28,
    )

    styles = getSampleStyleSheet()

    # Typography styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13.5,
        leading=16.5,
        textColor=colors.HexColor('#800000'),
        alignment=0,
    )

    sub_title_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#555555'),
        alignment=0,
    )

    h_sub = ParagraphStyle(
        'UnivSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#444444'),
    )

    cell_bold = ParagraphStyle(
        'CellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#111111'),
    )

    cell_norm = ParagraphStyle(
        'CellNorm',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#333333'),
    )

    elements = []

    # 1. Top Decorative Bar
    elements.append(HRFlowable(width="100%", thickness=3.5, color=colors.HexColor('#800000'), spaceAfter=8))

    # 2. Header Table: Logo on Left, Institutional Sub-lines, Reference Box on Right
    # uchicago_full_logo aspect ratio: 1112x238 (~4.67:1). Width 175, Height 37.5
    rl_logo = RLImage(logo_path, width=175, height=37.5)

    header_left = [
        rl_logo,
        Spacer(1, 4),
        Paragraph("<font color='#444444' size='7.5'>Office of the Bursar &amp; Student Accounts • Division of the Physical Sciences<br/>Searle Chemistry Laboratories • 5801 S. Ellis Avenue, Chicago, IL 60637 USA</font>", h_sub)
    ]

    header_right = [
        Paragraph("<font color='#800000'><strong>OFFICIAL INSTITUTIONAL RECEIPT</strong></font><br/>"
                  "<font color='#555555' size='7.5'>Tax Year: 2026–2027 • Form 1098-T Eligible<br/>"
                  f"Reference: <strong>{ref_num}</strong><br/>"
                  "Bursar Authorization: <strong>VERIFIED &amp; CLEARED</strong></font>",
                  ParagraphStyle('HRight', parent=h_sub, alignment=2))
    ]

    header_table = Table([[header_left, header_right]], colWidths=[335, 188])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    elements.append(header_table)
    elements.append(Spacer(1, 4))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#dddddd'), spaceAfter=8))

    # 3. Document Title
    elements.append(Paragraph(doc_title, title_style))
    elements.append(Paragraph(doc_subtitle, sub_title_style))
    elements.append(Spacer(1, 8))

    # 4. Summary Identification Grid
    summary_data = [
        [
            Paragraph("<strong>TRANSACTION IDENTIFIERS</strong>", cell_bold),
            Paragraph("<strong>SETTLEMENT &amp; PROGRAM DATES</strong>", cell_bold)
        ],
        [
            Paragraph(f"<strong>Transaction ID:</strong> {txn_id}<br/>"
                      f"<strong>Invoice Number:</strong> {inv_id}<br/>"
                      f"<strong>Bank Approval Code:</strong> {auth_code}<br/>"
                      f"<strong>Account Reference:</strong> {ref_num}<br/>"
                      "<strong>Issuing Channel:</strong> Bursar Direct Mandate Clearing", cell_norm),
            Paragraph(f"<strong>Settlement Status:</strong> <font color='#137333'><strong>CONFIRMED &amp; SETTLED (PAID)</strong></font><br/>"
                      f"<strong>Transaction Date:</strong> {txn_date}<br/>"
                      f"<strong>{secondary_date_label}</strong> {secondary_date_val}<br/>"
                      "<strong>Doctoral Matriculation:</strong> August 2027<br/>"
                      "<strong>Autumn Quarter Classes:</strong> September 2027", cell_norm)
        ]
    ]
    summary_table = Table(summary_data, colWidths=[260, 263])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#fbf7f7')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#ffffff')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#d9c5c5')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#eeeeee')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    elements.append(summary_table)
    elements.append(Spacer(1, 8))

    # 5. Candidate & Billing Details
    cand_data = [
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
    cand_table = Table(cand_data, colWidths=[260, 263])
    cand_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#fbf7f7')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#ffffff')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#d9c5c5')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#eeeeee')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    elements.append(cand_table)
    elements.append(Spacer(1, 8))

    # 6. Itemized Table
    item_header = [
        Paragraph("<font color='#ffffff'><strong>ITEM CODE</strong></font>", cell_bold),
        Paragraph("<font color='#ffffff'><strong>DESCRIPTION &amp; DESIGNATION</strong></font>", cell_bold),
        Paragraph("<font color='#ffffff'><strong>TERM</strong></font>", cell_bold),
        Paragraph("<font color='#ffffff'><strong>AMOUNT (USD)</strong></font>", ParagraphStyle('RBold', parent=cell_bold, alignment=2)),
    ]

    item_row_1 = [
        Paragraph(f"<strong>{item_code}</strong>", cell_bold),
        Paragraph(item_desc, cell_norm),
        Paragraph(item_term, cell_norm),
        Paragraph(f"<strong>{item_amt}</strong>", ParagraphStyle('RCell', parent=cell_bold, alignment=2)),
    ]

    item_subtotal = [
        "", Paragraph("Subtotal", cell_bold), "",
        Paragraph(f"<strong>{item_amt}</strong>", ParagraphStyle('RCell', parent=cell_bold, alignment=2))
    ]

    item_remission = [
        "", Paragraph("Departmental Fellowship Remission (Tuition Offset Applied)", cell_norm), "",
        Paragraph("-$0.00", ParagraphStyle('RNorm', parent=cell_norm, alignment=2))
    ]

    item_total = [
        "",
        Paragraph(f"<font size='9.5'><strong>TOTAL PAID (SETTLED IN FULL):</strong></font><br/><font color='#555555' size='7'>({amount_words})</font>", cell_bold),
        "",
        Paragraph(f"<font color='#800000' size='11'><strong>{total_amt}</strong></font>", ParagraphStyle('RTotal', parent=cell_bold, alignment=2))
    ]

    items_data = [item_header, item_row_1, item_subtotal, item_remission, item_total]
    items_table = Table(items_data, colWidths=[90, 260, 85, 88])
    items_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#800000')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#800000')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e5e5e5')),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#fcf8f8')),
        ('LINEABOVE', (0,-1), (-1,-1), 1.5, colors.HexColor('#800000')),
        ('TOPPADDING', (0,0), (-1,-1), 4.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(items_table)
    elements.append(Spacer(1, 8))

    # 7. Payment Instrument & Mandate Details
    mandate_data = [
        [
            Paragraph("<strong>PAYMENT INSTRUMENT &amp; CLEARING MANDATE</strong>", cell_bold),
            Paragraph("<strong>SETTLEMENT CONFIRMATION</strong>", cell_bold)
        ],
        [
            Paragraph(f"<strong>Method:</strong> {payment_desc}<br/>"
                      "<strong>Pre-Authorization Status:</strong> Verified &amp; Pre-Authorized Mandate Active<br/>"
                      "<strong>Issuing Institution:</strong> Stanford Federal Credit Union / Global Partner Bank<br/>"
                      "<strong>Cardholder Auth Name:</strong> Devendra Dubey • Expiry: 04/32", cell_norm),
            Paragraph("<strong>Clearing Engine:</strong> University of Chicago Institutional Gateway<br/>"
                      f"<strong>Gateway Batch Ref:</strong> BATCH-UCHI-2026-OCT<br/>"
                      f"<strong>Ledger Entry:</strong> BUR-2026-{txn_id[-6:]} • CLEARED<br/>"
                      "<strong>Dispute / Chargeback Hold:</strong> Zero Liability Mandate Active", cell_norm)
        ]
    ]
    mandate_table = Table(mandate_data, colWidths=[260, 263])
    mandate_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#fbf7f7')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#ffffff')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#d9c5c5')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#eeeeee')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    elements.append(mandate_table)
    elements.append(Spacer(1, 8))

    # 8. Verification QR Code & Official Bursar Signatures
    rl_qr = RLImage(qr_path, width=54, height=54)

    footer_text = Paragraph(
        "<strong>INSTITUTIONAL VALIDATION SEAL &amp; MANDATE POLICY</strong><br/>"
        "This official tax receipt and enrollment mandate confirmation is electronically issued under the authority "
        "of the Office of the Bursar, The University of Chicago. Scan the QR code to verify this record on the live "
        "Student Accounts registry. <b>Policy Terms:</b> Seat confirmation fee ($6,200.00 USD) is reimbursable/refundable "
        "<b>ONLY in case of non-admission</b> (e.g. visa denial or cancellation); upon enrollment, it is mandatory and non-reimbursable. "
        "IRS Form 1098-T eligible.",
        ParagraphStyle('FNotice', parent=styles['Normal'], fontName='Helvetica', fontSize=6.5, leading=8.5, textColor=colors.HexColor('#555555'))
    )

    sig_block = Paragraph(
        "<font size='7.5'><strong>OFFICE OF THE BURSAR</strong><br/>"
        "Division of the Physical Sciences<br/>"
        "<font color='#137333'><strong>[ELECTRONICALLY SIGNED &amp; SEALED]</strong></font><br/>"
        f"Validation Code: {auth_code}</font>",
        ParagraphStyle('FSig', parent=styles['Normal'], fontName='Helvetica', fontSize=7.5, leading=9.5, textColor=colors.HexColor('#333333'), alignment=2)
    )

    verif_data = [[rl_qr, footer_text, sig_block]]
    verif_table = Table(verif_data, colWidths=[62, 300, 161])
    verif_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 2),
        ('RIGHTPADDING', (0,0), (-1,-1), 2),
    ]))
    elements.append(verif_table)

    # 9. Bottom Red Rule
    elements.append(Spacer(1, 4))
    elements.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#800000'), spaceAfter=0))

    # Build PDF
    doc.build(elements)
    print(f"Generated PDF at {pdf_path}")

    # Render 144 DPI high quality preview image using pymupdf
    pdf_doc = pymupdf.open(pdf_path)
    page = pdf_doc[0]
    pix = page.get_pixmap(dpi=144)
    pix.save(img_path)
    print(f"Rendered PNG preview at {img_path} ({pix.width}x{pix.height})")

if __name__ == "__main__":
    build_pdf_invoice("seat_deposit")
    build_pdf_invoice("application_fee")
    print("Both official invoices built successfully!")
