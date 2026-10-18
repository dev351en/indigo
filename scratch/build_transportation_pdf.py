from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

pdf_path = "site_1to1/assets/documents/2024-transportation-and-parking-guide.pdf"

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    rightMargin=40, leftMargin=40,
    topMargin=40, bottomMargin=40
)

styles = getSampleStyleSheet()

maroon = colors.HexColor("#800000")
charcoal = colors.HexColor("#222222")
warm_grey = colors.HexColor("#f8f9fa")
border_grey = colors.HexColor("#dcdcdc")

title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=22,
    leading=26,
    textColor=maroon,
    spaceAfter=6
)

subtitle_style = ParagraphStyle(
    'DocSubtitle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=11,
    leading=15,
    textColor=colors.HexColor("#555555"),
    spaceAfter=15
)

section_heading = ParagraphStyle(
    'SectionHeading',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=14,
    leading=18,
    textColor=maroon,
    spaceBefore=12,
    spaceAfter=8
)

body_style = ParagraphStyle(
    'BodyText',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9.5,
    leading=14,
    textColor=charcoal,
    spaceAfter=6
)

callout_style = ParagraphStyle(
    'CalloutText',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=9,
    leading=13,
    textColor=colors.HexColor("#444444")
)

story = []

# PAGE 1: Campus Shuttles & Safe Transit
header_table_data = [
    [Paragraph("<b>THE UNIVERSITY OF CHICAGO</b><br/><font size=9 color='#666666'>Department of Safety & Security &bull; Transportation & Parking Services</font>", body_style),
     Paragraph("<font color='#800000'><b>2024–2025 TRANSIT GUIDE</b></font><br/><font size=8 color='#888888'>Updated Autumn Quarter 2024</font>", ParagraphStyle('RAlign', parent=body_style, alignment=2))]
]
header_table = Table(header_table_data, colWidths=[350, 182])
header_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LINEBELOW', (0,0), (-1,-1), 1.5, maroon)
]))
story.append(header_table)
story.append(Spacer(1, 15))

story.append(Paragraph("Campus Transportation & Safety Escort Guide", title_style))
story.append(Paragraph("Comprehensive navigation and safety transit protocols for University of Chicago students, faculty, staff, and campus visitors across Hyde Park and adjacent medical facilities.", subtitle_style))

story.append(Paragraph("1. UGo Daytime & NightRide Shuttle Services", section_heading))
story.append(Paragraph("The University operates an extensive network of scheduled and demand-responsive shuttle services that operate throughout the Hyde Park community and university campus free of charge for UChicago ID holders.", body_style))

shuttle_data = [
    [Paragraph("<b>Service Route</b>", body_style), Paragraph("<b>Operating Hours</b>", body_style), Paragraph("<b>Frequency</b>", body_style), Paragraph("<b>Coverage Area</b>", body_style)],
    [Paragraph("<b>UGo Daytime Shuttles</b><br/>(Apostles, Midway, 53rd St)", body_style), Paragraph("Monday–Friday<br/>7:00 AM – 6:00 PM", body_style), Paragraph("Every 10–15 mins", body_style), Paragraph("Campus central quads, Medical Center, 53rd St business corridor", body_style)],
    [Paragraph("<b>UGo NightRide Network</b><br/>(North, South, East, Central)", body_style), Paragraph("Daily (7 days/wk)<br/>5:00 PM – 4:00 AM", body_style), Paragraph("Every 15–20 mins", body_style), Paragraph("Residential corridors, Regenstein Library, South Campus Garages", body_style)],
    [Paragraph("<b>Friend Center Route</b>", body_style), Paragraph("Monday–Friday<br/>6:00 AM – 9:00 PM", body_style), Paragraph("Every 20 mins", body_style), Paragraph("Hospital clinics, 5801 S Ellis, Graham School, Center for Care", body_style)]
]
shuttle_table = Table(shuttle_data, colWidths=[130, 110, 100, 192])
shuttle_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f4ecec")),
    ('TEXTCOLOR', (0,0), (-1,0), maroon),
    ('GRID', (0,0), (-1,-1), 0.5, border_grey),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('VALIGN', (0,0), (-1,-1), 'TOP')
]))
story.append(shuttle_table)
story.append(Spacer(1, 12))

story.append(Paragraph("2. Live Tracking & Safety Escort Services", section_heading))
story.append(Paragraph("<b>Real-Time Tracking:</b> Download the <b>TransLoc 3D Transit App</b> or visit <i>ugo.uchicago.edu</i> to track live bus positions, route detours, and arrival predictions.", body_style))
story.append(Paragraph("<b>University Safety Escort Program:</b> Any university community member concerned about traveling alone after dark may request a walking escort 24 hours a day, 7 days a week. Uniformed University of Chicago Police Department (UCPD) officers or safety ambassadors will meet you at any campus building and accompany you to your vehicle or campus residence.", body_style))

escort_box = [
    [Paragraph("<b>24/7 SAFETY ESCORT DISPATCH:</b> (773) 702-8181 &bull; <b>EMERGENCY POLICE:</b> (773) 702-8181 or 911<br/><font size=8.5 color='#555555'>Over 400 Emergency Blue Light Phones are distributed across campus with instantaneous direct dispatch connectivity.</font>", callout_style)]
]
escort_table = Table(escort_box, colWidths=[532])
escort_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#fcf4f4")),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#800000")),
    ('PADDING', (0,0), (-1,-1), 8)
]))
story.append(escort_table)

story.append(PageBreak())

# PAGE 2: Campus Parking Garages, CTA Connections & Permits
header_table_data2 = [
    [Paragraph("<b>THE UNIVERSITY OF CHICAGO</b><br/><font size=9 color='#666666'>Department of Safety & Security &bull; Transportation & Parking Services</font>", body_style),
     Paragraph("<font color='#800000'><b>CAMPUS PARKING & TRANSIT</b></font><br/><font size=8 color='#888888'>Page 2 of 2</font>", ParagraphStyle('RAlign2', parent=body_style, alignment=2))]
]
header_table2 = Table(header_table_data2, colWidths=[350, 182])
header_table2.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LINEBELOW', (0,0), (-1,-1), 1.5, maroon)
]))
story.append(header_table2)
story.append(Spacer(1, 15))

story.append(Paragraph("3. Campus Parking Facilities & Visitor Rates", section_heading))
story.append(Paragraph("The University operates multiple parking structures and surface lots. Automated pay-by-cell stations and credit card payment gates accept Visa, Mastercard, Discover, and American Express.", body_style))

parking_data = [
    [Paragraph("<b>Facility Name</b>", body_style), Paragraph("<b>Location Address</b>", body_style), Paragraph("<b>Capacity / Features</b>", body_style), Paragraph("<b>Visitor Hourly Rates</b>", body_style)],
    [Paragraph("<b>Ellis Garage</b>", body_style), Paragraph("5525 S. Ellis Ave.<br/>(Near Ratner & Quad)", body_style), Paragraph("1,050 spaces<br/>EV charging stations", body_style), Paragraph("0-2 hrs: $10<br/>2-4 hrs: $16<br/>Daily Max: $25", body_style)],
    [Paragraph("<b>Campus South Garage</b>", body_style), Paragraph("6054 S. Drexel Ave.<br/>(Near Booth & Law)", body_style), Paragraph("1,400 spaces<br/>Direct shuttle connect", body_style), Paragraph("0-2 hrs: $10<br/>2-4 hrs: $16<br/>Daily Max: $25", body_style)],
    [Paragraph("<b>Medical Center Garage</b>", body_style), Paragraph("5840 S. Maryland Ave.<br/>(Center for Care)", body_style), Paragraph("1,200 spaces<br/>Patient priority & valet", body_style), Paragraph("Validated Patient: $10<br/>Visitor Daily: $24", body_style)],
    [Paragraph("<b>Wells Surface Lot</b>", body_style), Paragraph("South University Ave.", body_style), Paragraph("Permit holders / Evenings", body_style), Paragraph("Free after 4:00 PM M-F<br/>Weekends Free", body_style)]
]
parking_table = Table(parking_data, colWidths=[120, 130, 142, 140])
parking_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f4ecec")),
    ('TEXTCOLOR', (0,0), (-1,0), maroon),
    ('GRID', (0,0), (-1,-1), 0.5, border_grey),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('VALIGN', (0,0), (-1,-1), 'TOP')
]))
story.append(parking_table)
story.append(Spacer(1, 14))

story.append(Paragraph("4. Chicago Transit Authority (CTA) Public Transit", section_heading))
story.append(Paragraph("UChicago maintains a special partnership with the Chicago Transit Authority (CTA). UChicago students, staff, and faculty ride several CTA routes serving campus free of charge upon tapping a valid UChicago ID or mobile transit pass:", body_style))

cta_points = [
    Paragraph("&bull; <b>Route 171 (U. of Chicago / Hyde Park):</b> Connects Ellis Garage, 55th/57th Street Metra stations, Regenstein Library, and Woodlawn residential buildings.", body_style),
    Paragraph("&bull; <b>Route 172 (U. of Chicago / Kenwood):</b> Circulates between main quad, East 53rd Street shopping district, and North Hyde Park.", body_style),
    Paragraph("&bull; <b>Route 55 (Garfield):</b> Provides direct East-West connectivity to the Garfield Red Line and Green Line rapid transit stations.", body_style),
    Paragraph("&bull; <b>Metra Electric Line:</b> Fast commuter rail connection between Hyde Park (57th/59th St stations) and Millennium Station in downtown Chicago (15-20 min transit time).", body_style)
]
for p in cta_points:
    story.append(p)

story.append(Spacer(1, 14))
footer_notice = [
    [Paragraph("<b>Institutional Inquiries:</b> Parking & Transportation Services Office &bull; 5525 S. Ellis Ave, Suite 171 &bull; Phone: (773) 702-8969 &bull; Email: <i>parking@uchicago.edu</i> &bull; Web: <i>visit.uchicago.edu</i>", callout_style)]
]
footer_table = Table(footer_notice, colWidths=[532])
footer_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f9f9f9")),
    ('BOX', (0,0), (-1,-1), 0.5, border_grey),
    ('PADDING', (0,0), (-1,-1), 6)
]))
story.append(footer_table)

doc.build(story)
print(f"Generated {pdf_path} successfully!")
