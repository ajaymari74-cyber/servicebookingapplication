import os
import sys
import shutil
import subprocess

BRAIN_DIR = r"C:\Users\ajayt\.gemini\antigravity-ide\brain\e77ba1c9-97f5-4798-a709-59b023d29742"
DOC_DIR = r"d:\Fontend Projects\serviq"
SCREENSHOTS_DIR = os.path.join(DOC_DIR, "documentation_screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

# Copy and rename screenshots
SCREENSHOT_MAP = {
    "01_home_page.png": "home_page_1789662048922.png",
    "02_all_services_catalog.png": "all_services_page_1789662088529.png",
    "03_service_details_electrician.png": "service_details_electrician_1789662062294.png",
    "04_service_details_pest_control_gallery.png": "service_details_pest_control_1789662074837.png",
    "05_schedule_appointment_booking.png": "booking_page_1789662103120.png",
    "06_booking_confirmed_receipt.png": "booking_success_page_1789662202186.png",
    "07_my_bookings_dashboard.png": "my_bookings_page_1789662218726.png",
}

for target_name, src_name in SCREENSHOT_MAP.items():
    src_path = os.path.join(BRAIN_DIR, src_name)
    dst_path = os.path.join(SCREENSHOTS_DIR, target_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"Copied {src_name} -> {target_name}")
    else:
        print(f"Warning: {src_path} not found")

# Ensure python-docx is installed
try:
    import docx
except ImportError:
    print("Installing python-docx...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-docx"])
    import docx

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, color_hex):
    shading_xml = f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>'
    cell._tc.get_or_add_tcPr().append(parse_xml(shading_xml))

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_documentation():
    doc = Document()

    # Set standard margins (1 inch)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Base styles
    primary_color = RGBColor(30, 58, 138)    # Deep Navy / #1e3a8a
    secondary_color = RGBColor(14, 116, 144) # Dark Cyan / #0e7490
    dark_gray = RGBColor(51, 65, 85)         # Slate / #334155
    body_color = RGBColor(30, 41, 59)        # #1e293b

    # ==========================================
    # COVER / TITLE SECTION
    # ==========================================
    p_pre = doc.add_paragraph()
    p_pre.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_pre = p_pre.add_run("PROJECT TECHNICAL DOCUMENTATION")
    r_pre.font.name = "Calibri"
    r_pre.font.size = Pt(13)
    r_pre.font.bold = True
    r_pre.font.color.rgb = secondary_color
    p_pre.paragraph_format.space_before = Pt(36)
    p_pre.paragraph_format.space_after = Pt(8)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("ServIQ – On-Demand Doorstep Home & Electrical Services Booking Platform")
    r_title.font.name = "Calibri"
    r_title.font.size = Pt(24)
    r_title.font.bold = True
    r_title.font.color.rgb = primary_color
    p_title.paragraph_format.space_after = Pt(12)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("A High-Performance, Responsive React.js Web Application with Instant Time-Slot Scheduling, Interactive Image Gallery & LocalStorage Data Persistence")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(12)
    r_sub.font.italic = True
    r_sub.font.color.rgb = dark_gray
    p_sub.paragraph_format.space_after = Pt(36)

    # Author Box Table
    author_table = doc.add_table(rows=4, cols=2)
    author_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    author_table.autofit = False

    info_data = [
        ("Prepared By:", "Ajay M"),
        ("Designation / Role:", "Junior Software Developer"),
        ("Project Stack:", "React.js, Vite, JavaScript (ES6+), CSS3, React Router v6"),
        ("Document Version & Date:", "Version 1.0 (Production Release) | September 2026")
    ]

    for i, (label, val) in enumerate(info_data):
        row = author_table.rows[i]
        c1 = row.cells[0]
        c2 = row.cells[1]
        c1.width = Inches(2.2)
        c2.width = Inches(4.3)
        set_cell_background(c1, "F1F5F9")
        set_cell_background(c2, "FFFFFF")
        set_cell_margins(c1, 100, 100, 150, 150)
        set_cell_margins(c2, 100, 100, 150, 150)

        p1 = c1.paragraphs[0]
        r1 = p1.add_run(label)
        r1.font.name = "Calibri"
        r1.font.bold = True
        r1.font.size = Pt(10.5)
        r1.font.color.rgb = dark_gray

        p2 = c2.paragraphs[0]
        r2 = p2.add_run(val)
        r2.font.name = "Calibri"
        if i == 0:
            r2.font.bold = True
            r2.font.color.rgb = primary_color
        elif i == 1:
            r2.font.bold = True
            r2.font.color.rgb = secondary_color
        else:
            r2.font.color.rgb = body_color
        r2.font.size = Pt(10.5)

    doc.add_page_break()

    def add_section_header(number_str, title_str):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(f"{number_str} {title_str}")
        run.font.name = "Calibri"
        run.font.size = Pt(16)
        run.font.bold = True
        run.font.color.rgb = primary_color
        return p

    def add_subsection_header(sub_num, sub_title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(f"{sub_num} {sub_title}")
        run.font.name = "Calibri"
        run.font.size = Pt(13)
        run.font.bold = True
        run.font.color.rgb = secondary_color
        return p

    def add_body_paragraph(text, bold_prefix="", italic=False):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_bold = p.add_run(bold_prefix + " ")
            r_bold.font.name = "Calibri"
            r_bold.font.size = Pt(11)
            r_bold.font.bold = True
            r_bold.font.color.rgb = body_color
        r_text = p.add_run(text)
        r_text.font.name = "Calibri"
        r_text.font.size = Pt(11)
        r_text.font.italic = italic
        r_text.font.color.rgb = body_color
        return p

    def add_bullet(text, bold_prefix=""):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_b = p.add_run(bold_prefix + ": ")
            r_b.font.name = "Calibri"
            r_b.font.size = Pt(11)
            r_b.font.bold = True
            r_b.font.color.rgb = dark_gray
        r_t = p.add_run(text)
        r_t.font.name = "Calibri"
        r_t.font.size = Pt(11)
        r_t.font.color.rgb = body_color
        return p

    def add_code_block(code_text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.left_indent = Inches(0.25)
        run = p.add_run(code_text)
        run.font.name = "Consolas"
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(15, 23, 42)
        return p

    def add_image_figure(img_path, caption_text):
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(4)
            doc.add_picture(img_path, width=Inches(6.0))
            last_p = doc.paragraphs[-1]
            last_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(2)
            p_cap.paragraph_format.space_after = Pt(14)
            r_cap = p_cap.add_run(f"Figure: {caption_text}")
            r_cap.font.name = "Calibri"
            r_cap.font.size = Pt(9.5)
            r_cap.font.bold = True
            r_cap.font.italic = True
            r_cap.font.color.rgb = dark_gray
        else:
            add_body_paragraph(f"[Image placeholder: {caption_text}]")

    # ==========================================
    # 1. INTRODUCTION
    # ==========================================
    add_section_header("1.", "Introduction")
    add_body_paragraph(
        "ServIQ is a modern, full-featured on-demand home and electrical services web application developed using React.js and modern frontend tooling. In modern urban living, finding qualified, background-verified, and punctual technicians for everyday domestic repairs—such as electricians, master plumbers, air conditioner technicians, home deep cleaners, carpenters, and appliance mechanics—remains a major friction point for consumers. ServIQ bridges this gap by delivering a frictionless, transparent, and ultra-reliable digital booking ecosystem directly from any web browser."
    )
    add_body_paragraph(
        "The application provides complete end-to-end service lifecycle operations:",
        bold_prefix="Core Capabilities:"
    )
    add_bullet("Service Catalog Discovery", "Comprehensive discovery of doorstep services across 8 specialized domestic domains.")
    add_bullet("Instant Keyword Search & Category Filtering", "Dynamic multi-criteria search by service name, category, and description.")
    add_bullet("Sorting Capabilities", "Sort services by popularity/recommendation, customer rating, and price (low-to-high, high-to-low).")
    add_bullet("Rich Visual Presentation & Image Gallery", "High-resolution photography for each service with an interactive multi-view photo gallery for specialized services such as Pest Control & Sanitization.")
    add_bullet("Deep Detailed View", "Full breakdown of service pricing, inclusions, time duration, certified badges, warranty coverage, and customer assurances.")
    add_bullet("3-Step Hassle-Free Booking Engine", "Pick preferred date and time slots, input contact details and street address, and select payment method (Pay after Service or Pay Online).")
    add_bullet("Official Booking Receipt Generation", "Automatic creation of verifiable booking confirmation cards with unique IDs (e.g., #SRV-15376).")
    add_bullet("Persistent Client-Side Booking Management", "Full management dashboard ('My Bookings') with status tab filtering (All, Confirmed, Completed, Cancelled) and instant modal-confirmed appointment cancellations.")

    # ==========================================
    # 2. OBJECTIVES
    # ==========================================
    add_section_header("2.", "Objectives")
    add_body_paragraph("The primary technical and operational objectives of the ServIQ project are:")
    objectives = [
        ("Responsive & Modern UI Architecture", "To develop an aesthetically rich, ultra-fast, and responsive web user interface tailored for homeowners and service requesters across desktops, tablets, and smartphones."),
        ("Component-Based Modularity", "To design clean, decoupled, and highly reusable React components (ServiceCard, ServiceList, BookingForm, NavBar, Footer, Button) adhering to standard software engineering separation of concerns."),
        ("Centralized Client-Side State Management", "To master and implement React state handling mechanisms utilizing React Hooks (useState, useEffect, useMemo) and React Context API for global authentication and customer session tracking."),
        ("Persistent Local Storage Architecture", "To establish a reliable, zero-latency client-side persistence layer utilizing browser LocalStorage for appointment schedules, user authentication tokens, and initial pre-seeded sample data."),
        ("Dynamic Client-Side Routing", "To structure fluid, seamless multi-page transitions and deep-linking using React Router v6 without full-page reloads."),
        ("Rich Media Asset Integration", "To integrate authentic high-definition service photography across all application components (Card Banners, Hero Details, Order Summary, Receipt, and Booking Cards), elevating user trust and visual appeal."),
        ("Transparent User-Centric Flow", "To provide upfront fixed pricing with zero hidden diagnostic fees, immediate date/time confirmation, and 'Pay After Service' convenience.")
    ]
    for i, (title, desc) in enumerate(objectives, 1):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(4)
        r_num = p.add_run(f"{i}. {title}: ")
        r_num.font.name = "Calibri"
        r_num.font.size = Pt(11)
        r_num.font.bold = True
        r_num.font.color.rgb = dark_gray
        r_desc = p.add_run(desc)
        r_desc.font.name = "Calibri"
        r_desc.font.size = Pt(11)
        r_desc.font.color.rgb = body_color

    # ==========================================
    # 3. TECHNOLOGIES USED
    # ==========================================
    add_section_header("3.", "Technologies Used")
    add_body_paragraph("ServIQ was constructed leveraging industry-standard modern frontend tools, libraries, and frameworks:")

    tech_table = doc.add_table(rows=1, cols=3)
    tech_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    tech_table.autofit = False

    hdr_cells = tech_table.rows[0].cells
    hdr_cells[0].width = Inches(1.8)
    hdr_cells[1].width = Inches(1.8)
    hdr_cells[2].width = Inches(2.9)

    headers = ["Technology", "Category", "Purpose in ServIQ"]
    for i, h in enumerate(headers):
        set_cell_background(hdr_cells[i], "1E3A8A")
        set_cell_margins(hdr_cells[i], 120, 120, 150, 150)
        p = hdr_cells[i].paragraphs[0]
        r = p.add_run(h)
        r.font.name = "Calibri"
        r.font.bold = True
        r.font.size = Pt(10.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    tech_data = [
        ("React.js (v19)", "UI Library", "Component-based declarative user interface construction and virtual DOM rendering."),
        ("Vite (v6)", "Build Tool / Dev Server", "Ultra-fast Hot Module Replacement (HMR) and optimized ES module bundling."),
        ("JavaScript (ES6+)", "Core Language", "Application logic, state manipulation, array filtering, and asynchronous actions."),
        ("HTML5", "Markup", "Semantic layout architecture, accessible form controls, and structured content."),
        ("CSS3", "Styling & Design System", "Custom color variables, responsive flexbox & grid systems, glassmorphism, and micro-interactions."),
        ("React Router (v6)", "Client Routing", "Declarative browser history routing, parameterized URL matching, and smooth page switches."),
        ("React Context API", "State Management", "Global authentication state propagation across all component hierarchies."),
        ("LocalStorage API", "Data Persistence", "Synchronous local client-side persistence for booking records and user profiles."),
        ("VS Code", "Development IDE", "Source code authoring, linting, debugging, and extensions integration."),
        ("Git / GitHub", "Version Control", "Distributed version control and source code repository management.")
    ]

    for row_idx, (t, c, pur) in enumerate(tech_data):
        row = tech_table.add_row()
        bg_col = "F8FAFC" if row_idx % 2 == 0 else "FFFFFF"
        for col_idx, text in enumerate([t, c, pur]):
            cell = row.cells[col_idx]
            cell.width = [Inches(1.8), Inches(1.8), Inches(2.9)][col_idx]
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, 80, 80, 120, 120)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.name = "Calibri"
            r.font.size = Pt(9.5)
            if col_idx == 0:
                r.font.bold = True
                r.font.color.rgb = primary_color
            else:
                r.font.color.rgb = body_color

    # ==========================================
    # 4. SYSTEM REQUIREMENTS
    # ==========================================
    add_section_header("4.", "System Requirements")
    add_subsection_header("4.1", "Hardware Requirements")
    add_bullet("Processor", "Intel Core i3, AMD Ryzen 3 or higher (dual-core 2.0 GHz minimum).")
    add_bullet("RAM", "4 GB minimum (8 GB or higher strongly recommended for smooth dev server execution).")
    add_bullet("Storage Space", "10 GB of available hard disk / SSD space.")
    add_bullet("Display Resolution", "1366 x 768 minimum resolution (Full HD 1920 x 1080 recommended for testing responsive breakpoints).")

    add_subsection_header("4.2", "Software Requirements")
    add_bullet("Operating System", "Microsoft Windows 10 / Windows 11, macOS, or Linux distribution.")
    add_bullet("Node.js Runtime", "Node.js version 18.x or version 20.x LTS.")
    add_bullet("Package Manager", "npm (Node Package Manager) version 9.x or higher / yarn / pnpm.")
    add_bullet("Code Editor", "Visual Studio Code (recommended) or any modern JavaScript IDE.")
    add_bullet("Web Browser", "Google Chrome 110+, Microsoft Edge 110+, Mozilla Firefox 110+, or Apple Safari 16+.")

    # ==========================================
    # 5. PROJECT STRUCTURE
    # ==========================================
    add_section_header("5.", "Project Structure")
    add_body_paragraph("The ServIQ project adopts a clean, organized, and scalable architectural folder structure, segregating assets, reusable components, global contexts, mock datasets, page views, and storage utility functions:")

    project_tree = """serviq/
├── index.html                       # HTML5 Root Entry Point & SEO Metadata
├── package.json                     # Project Manifest & NPM Dependencies
├── vite.config.js                   # Vite Bundler & Build Configuration
│
├── public/                          # Static Web Assets (Favicon, Manifest)
│   └── vite.svg
│
└── src/                             # Main React Application Source
    ├── App.css                      # Global UI Design System, Tokens, Animations
    ├── App.jsx                      # Master Router Tree & Layout Assembly
    ├── index.css                    # Base Resets & Typography Tokens
    ├── main.jsx                     # React DOM Root Mounting & Context Providers
    │
    ├── assets/                      # Real Doorstep Service Photographic Assets
    │   ├── Ac cleaning.jpg
    │   ├── electriician services.jpg
    │   ├── Expert Carpentry & Furniture.jpg
    │   ├── Home Painting & Touch-up.jpg
    │   ├── housecleaning.jpg
    │   ├── Pest Control & Sanitization.jpg
    │   ├── Pest Control & Sanitization1.jpg
    │   ├── plumpingservice.jpg
    │   └── Washing Machine & Refrigerator Repair.jpg
    │
    ├── Components/                  # Reusable Modular UI Components
    │   ├── BookingForm.jsx          # 3-Step Scheduling Form with Order Summary
    │   ├── Button.jsx               # Universal Button Primitive (variants, sizes)
    │   ├── Footer.jsx               # Global Footer with Company & Trust Links
    │   ├── NavBar.jsx               # Sticky Top Navbar with Auth & Navigation
    │   ├── ServiceCard.jsx          # Service Card Banner with Price & Badges
    │   └── ServiceList.jsx          # Filter Pills, Search Bar, Sort & Card Grid
    │
    ├── context/                     # Global State Providers
    │   └── AuthContext.jsx          # Authentication Session & Current User State
    │
    ├── data/                        # Static Application Datasets
    │   └── servicesData.js          # Service Catalog, Inclusions, Pricing & Images
    │
    ├── pages/                       # Route Page Views
    │   ├── Booking.jsx              # Service Scheduling Page with Visual Spotlight
    │   ├── BookingSuccess.jsx       # Official Booking Confirmed Receipt (#SRV-XXXX)
    │   ├── Home.jsx                 # Landing Page (Hero, Popular Services, Steps)
    │   ├── Login.jsx                # User Login & Demo Credential Access
    │   ├── MyBookings.jsx           # Booking History Dashboard with Status Tabs
    │   ├── Register.jsx             # New Customer Registration Page
    │   ├── ServiceDetails.jsx       # Deep Service Inspector with Photo Gallery
    │   └── Services.jsx             # Full Services Catalog View
    │
    └── utils/                       # Helper & Persistence Libraries
        └── bookingStorage.js        # LocalStorage CRUD Functions for Bookings"""

    add_code_block(project_tree)

    # ==========================================
    # 6. DETAILED APPLICATION MODULES
    # ==========================================
    add_section_header("6.", "Application Modules")
    add_body_paragraph("ServIQ is partitioned into seven distinct, highly integrated functional modules that provide a complete, cohesive booking workflow:")

    add_subsection_header("6.1", "Home & Hero Module (Home.jsx)")
    add_body_paragraph(
        "The Home Module represents the primary landing gateway for visitors. It welcomes users with a compelling headline, a highlighted trust badge ('Fast & Trusted Home Services'), and an integrated quick-search form. Directly beneath the hero header, visitors can click popular category pills ('Electrical', 'Plumbing', 'Cleaning', 'AC & Appliances', 'Pest Control') to quickly filter their desired service. The 'Popular Services' section showcases the top six doorstep repair offerings rendered with live photography, upfront prices, and ratings. The page also features a 'How It Works' 3-step visual guide (Choose Service -> Pick Date & Time -> Pay After Service), a 'Why Homeowners Trust Us' value section, and an interactive Call to Action banner."
    )

    add_subsection_header("6.2", "Service Catalog & Filtering Module (Services.jsx & ServiceList.jsx)")
    add_body_paragraph(
        "The Service Catalog Module displays all eight domestic services in a high-density, responsive grid. It includes interactive filter pills for all eight categories (All, Electrical, Plumbing, AC & Appliances, Cleaning, Pest Control, Painting, Carpentry). A real-time debounce-free instant search input searches across service titles, descriptions, and categories. Users can also sort the entire catalog using the 'Sort by' dropdown (Recommended, Highest Rated, Price: Low to High, Price: High to Low). When no matching results are found, an intuitive 'No Services Found' empty state offers a single-click 'Clear Filters' button."
    )

    add_subsection_header("6.3", "Service Details & Interactive Gallery Module (ServiceDetails.jsx)")
    add_body_paragraph(
        "The Service Details Module presents in-depth technical and logistical information for a selected service. At the top of the main column, a high-resolution 340px featured banner displays the service's real image along with category and highlight badges. For services with multiple photographs (such as Pest Control & Sanitization), an interactive thumbnail gallery allows the customer to preview multiple aspects of the service. Below the image, the module outlines the service rating, reviews count, typical duration, comprehensive description, a checklist of 'What's Included in this Service', and the 'ServIQ Service Promise' (30-day warranty, verified experts, transparent spares). The sticky right sidebar displays the fixed upfront price, strikethrough original price, and a direct 'Book Now (Pick Time Slot)' button."
    )

    add_subsection_header("6.4", "Appointment Scheduling & Booking Module (Booking.jsx & BookingForm.jsx)")
    add_body_paragraph(
        "The Booking Module provides an intuitive, step-by-step appointment configuration screen. It features a top 'Service Spotlight' banner that displays the chosen service image, price, duration, and ratings, while providing a dropdown to seamlessly switch services on the fly. The scheduling form is split into three simple steps:",
        bold_prefix="3-Step Configuration Flow:"
    )
    add_bullet("Step 1 (Date & Time)", "Interactive date picker defaulting to tomorrow (disallowing past dates) and a grid of 6 standard time slots (09:00 AM, 11:00 AM, 01:00 PM, 03:00 PM, 05:00 PM, 07:00 PM).")
    add_bullet("Step 2 (Customer Details & Location)", "Full name, phone number, multi-line street address, and optional landmark (auto-populated if user is logged in).")
    add_bullet("Step 3 (Payment Preference)", "Radio button selection between '💵 Pay after Service' (cash or UPI post-inspection) and '💳 Pay Online' (instant contactless checkout).")
    add_body_paragraph("A real-time 'Booking Summary' card on the right keeps the customer informed of the chosen service thumbnail, scheduled date, time slot, and total cost.")

    add_subsection_header("6.5", "Booking Confirmation & Official Receipt Module (BookingSuccess.jsx)")
    add_body_paragraph(
        "Upon successful appointment creation, the customer is immediately redirected to the Booking Success page. This module renders a high-trust verification receipt displaying a green success badge, an auto-generated unique tracking ID (e.g. #SRV-15376), a thumbnail of the booked service, the appointment date and time, the customer name, total amount payable, and physical address. Action buttons provide instant navigation to 'View in My Bookings', 'Book Another Service', or return to the 'Home' screen."
    )

    add_subsection_header("6.6", "My Bookings Management Dashboard Module (MyBookings.jsx)")
    add_body_paragraph(
        "The My Bookings Module acts as the customer's personal self-service hub. A filter tab bar enables fast filtering across four states: 'All', 'Confirmed', 'Completed', and 'Cancelled', with live count badges on each tab. Each booking card displays the service's photo, service name, status badge, booking ID, destination address, scheduled date and time, and price. For active confirmed appointments, customers can click a red 'Cancel' button, triggering a confirmation modal dialog. Once confirmed, the booking status is instantaneously updated in LocalStorage and reflected on the UI without reloading the page."
    )

    add_subsection_header("6.7", "User Authentication & Profile Session Module (AuthContext.jsx & Login.jsx)")
    add_body_paragraph(
        "The Authentication Module provides persistent user sessions utilizing React Context. Users can register with their name, email, phone, and default address, or log in using demo credentials. When authenticated, the top Navbar displays the user's name with an avatar badge and a 'Log Out' button. Furthermore, the Booking Form automatically detects the active user session and pre-fills the customer name, phone number, and address fields, saving time during scheduling."
    )

    # ==========================================
    # 7. FUNCTIONAL REQUIREMENTS
    # ==========================================
    add_section_header("7.", "Functional Requirements")
    add_body_paragraph("The functional requirements specify the expected behaviors, input parameters, and system reactions across all key application features:")

    fn_reqs = [
        ("FR-1: Service Catalog Browsing", "The system shall display a full catalog of 8 doorstep domestic services with real photography, titles, categories, pricing, and ratings."),
        ("FR-2: Dynamic Category Filtering", "The system shall filter the displayed services instantaneously when any of the 8 category pills is selected."),
        ("FR-3: Instant Keyword Search", "The system shall dynamically filter services matching input text across service title, description, or category without requiring a page reload."),
        ("FR-4: Multi-Criteria Sorting", "The system shall sort services dynamically by popularity, highest rating, price low-to-high, or price high-to-low."),
        ("FR-5: Detailed Service Inspection", "The system shall display full service information upon clicking any service card, including duration, inclusions, service promises, and related services."),
        ("FR-6: Interactive Photo Gallery", "The system shall allow users to switch between multiple high-resolution photos for services that include a multi-image gallery."),
        ("FR-7: Slot & Date Selection", "The system shall prevent selecting past dates and allow choosing one of six 2-hour daily appointment slots."),
        ("FR-8: Customer Location Entry", "The system shall capture mandatory customer name, telephone number, and street address, rejecting submissions with missing required fields."),
        ("FR-9: Flexible Payment Preference", "The system shall offer both 'Pay after Service' and 'Pay Online' payment modes."),
        ("FR-10: Booking ID Generation & Receipt", "The system shall generate a unique numeric booking ID upon booking confirmation and display an itemized receipt."),
        ("FR-11: Booking History Management", "The system shall persist all created appointments in LocalStorage and display them under 'My Bookings'."),
        ("FR-12: Modal-Confirmed Cancellation", "The system shall provide a two-step confirmation modal when a user attempts to cancel a confirmed appointment, updating the record status to 'Cancelled'.")
    ]

    for req_id, req_desc in fn_reqs:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(4)
        r_id = p.add_run(req_id + ": ")
        r_id.font.name = "Calibri"
        r_id.font.size = Pt(10.5)
        r_id.font.bold = True
        r_id.font.color.rgb = secondary_color
        r_desc = p.add_run(req_desc)
        r_desc.font.name = "Calibri"
        r_desc.font.size = Pt(10.5)
        r_desc.font.color.rgb = body_color

    # ==========================================
    # 8. REACT CONCEPTS USED
    # ==========================================
    add_section_header("8.", "React Concepts Used")
    add_body_paragraph("The ServIQ application demonstrates advanced, clean implementation of core React.js paradigms, hooks, and architectural patterns:")

    add_subsection_header("8.1", "Functional Components & Reusable Props")
    add_body_paragraph("Every user interface element in ServIQ is constructed as an isolated functional component accepting typed props for reusability. For example, ServiceCard accepts a service object prop containing images, titles, and prices:")
    add_code_block("""// Example from src/Components/ServiceCard.jsx
const ServiceCard = ({ service }) => {
  return (
    <div className="service-card">
      <Link to={`/services/${service.id}`} className="service-card-image-wrap">
        <img src={service.image} alt={service.name} className="service-card-image" loading="lazy" />
        <span className="badge badge-blue service-card-tag">{service.category}</span>
      </Link>
      <div className="service-card-body">
        <h3 className="service-title">{service.name}</h3>
        <p className="service-description">{service.shortDesc}</p>
        <span className="service-price-current">₹{service.price}</span>
      </div>
    </div>
  );
};""")

    add_subsection_header("8.2", "Interactive State Management (useState)")
    add_body_paragraph("Interactive state is managed locally via useState hooks for search query inputs, active category filters, selected appointment slots, and interactive gallery image selection:")
    add_code_block("""// Example from src/pages/ServiceDetails.jsx
const [activeImage, setActiveImage] = React.useState(service?.image || null);
const [selectedCategory, setSelectedCategory] = useState("All");
const [searchQuery, setSearchQuery] = useState("");
const [sortBy, setSortBy] = useState("popular");""")

    add_subsection_header("8.3", "Performance Optimization with useMemo")
    add_body_paragraph("To avoid expensive recalculations and re-filtering of service cards on every minor UI re-render, ServIQ utilizes useMemo to recalculate filtered and sorted lists only when search or sort parameters change:")
    add_code_block("""// Example from src/Components/ServiceList.jsx
const filteredServices = useMemo(() => {
  let result = servicesData.filter((service) => {
    const matchesCategory = selectedCategory === "All" || service.category.toLowerCase() === selectedCategory.toLowerCase();
    const matchesSearch = service.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          service.description.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCategory && matchesSearch;
  });
  if (sortBy === "price-low") result.sort((a, b) => a.price - b.price);
  else if (sortBy === "price-high") result.sort((a, b) => b.price - a.price);
  else if (sortBy === "rating") result.sort((a, b) => b.rating - a.rating);
  return result;
}, [selectedCategory, searchQuery, sortBy]);""")

    add_subsection_header("8.4", "Side Effects & Data Synchronization (useEffect)")
    add_body_paragraph("Side effects such as loading initial booking data from LocalStorage, syncing URL route parameters, or auto-populating customer details are governed by useEffect:")
    add_code_block("""// Example from src/pages/MyBookings.jsx
useEffect(() => {
  setBookings(getStoredBookings());
}, []);""")

    add_subsection_header("8.5", "Global Session Management (useContext)")
    add_body_paragraph("User authentication state and current user credentials are provided at the root level via AuthContext and consumed by any child component with zero prop-drilling:")
    add_code_block("""// Example from src/Components/BookingForm.jsx
const { currentUser } = useAuth();
useEffect(() => {
  if (currentUser) {
    setCustomerName(currentUser.fullName || "");
    setCustomerPhone(currentUser.phone || "");
    setAddress(currentUser.address || "");
  }
}, [currentUser]);""")

    add_subsection_header("8.6", "Conditional Rendering")
    add_body_paragraph("Conditional rendering is utilized extensively for display toggles, such as rendering gallery thumbnail switchers only when multiple images exist, or rendering 'Clear Filters' when a search yields zero matches:")
    add_code_block("""{galleryImages.length > 1 && (
  <div className="service-details-gallery-row">
    {galleryImages.map((imgSrc, idx) => (
      <button key={idx} className={`gallery-thumb-btn ${activeImage === imgSrc ? "active" : ""}`}
              onClick={() => setActiveImage(imgSrc)}>
        <img src={imgSrc} alt="thumbnail" />
      </button>
    ))}
  </div>
)}""")

    # ==========================================
    # 9. ROUTING ARCHITECTURE
    # ==========================================
    add_section_header("9.", "Routing Architecture")
    add_body_paragraph("Client-side routing is powered by React Router v6, delivering instant page transitions without browser reloads:")

    route_table = doc.add_table(rows=1, cols=4)
    route_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    route_table.autofit = False

    r_hdrs = ["URL Path", "Target Component", "Parameters / Query", "Purpose & Page Role"]
    for i, h in enumerate(r_hdrs):
        cell = route_table.rows[0].cells[i]
        cell.width = [Inches(1.5), Inches(1.5), Inches(1.5), Inches(2.0)][i]
        set_cell_background(cell, "0E7490")
        set_cell_margins(cell, 120, 120, 120, 120)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "Calibri"
        r.font.bold = True
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(255, 255, 255)

    routes_data = [
        ("/", "Home", "None", "Landing page with hero, search, category pills & popular services."),
        ("/services", "Services", "?cat=Category&q=Search", "Full service catalog with filters, search, and sorting."),
        ("/services/:id", "ServiceDetails", "id: Service ID", "Deep service view with full-bleed hero banner & photo gallery."),
        ("/book/:id?", "Booking", "id: Service ID (Optional)", "Appointment scheduling screen with spotlight and 3-step form."),
        ("/booking-success", "BookingSuccess", "?id=Booking ID", "Official booking confirmed receipt with booking reference #SRV-XXXX."),
        ("/my-bookings", "MyBookings", "None", "Customer appointment dashboard with status tabs and cancellation modal."),
        ("/login", "Login", "None", "User authentication login form with demo credential support."),
        ("/register", "Register", "None", "New user onboarding and customer account creation.")
    ]

    for row_idx, (u, c, p_param, pur) in enumerate(routes_data):
        row = route_table.add_row()
        bg_col = "F8FAFC" if row_idx % 2 == 0 else "FFFFFF"
        for col_idx, text in enumerate([u, c, p_param, pur]):
            cell = row.cells[col_idx]
            cell.width = [Inches(1.5), Inches(1.5), Inches(1.5), Inches(2.0)][col_idx]
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, 80, 80, 100, 100)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.name = "Calibri"
            r.font.size = Pt(9.5)
            if col_idx == 0:
                r.font.bold = True
                r.font.color.rgb = primary_color
            elif col_idx == 1:
                r.font.bold = True
                r.font.color.rgb = secondary_color
            else:
                r.font.color.rgb = body_color

    # ==========================================
    # 10. DATA ARCHITECTURE & STORAGE DESIGN
    # ==========================================
    add_section_header("10.", "Data Architecture & Storage Design")
    add_body_paragraph("ServIQ employs a decoupled data architecture where static service definitions are separated from dynamic user appointment records:")

    add_subsection_header("10.1", "Service Entity Schema (src/data/servicesData.js)")
    add_body_paragraph("Each service entity is modeled with complete logistical, financial, and media properties:")
    add_code_block("""{
  id: 1,
  name: "Professional Electrician",
  category: "Electrical",
  icon: "⚡",
  image: electricianImg,          // Imported real photographic asset
  gallery: [pestImg, pestImg2],   // Optional multi-image array for gallery services
  shortDesc: "Complete electrical repairs, wiring, switches & appliance installations.",
  description: "Certified electricians equipped to handle complete home and office needs...",
  price: 499,
  originalPrice: 799,
  rating: 4.8,
  reviewsCount: 342,
  duration: "45 - 60 mins",
  badge: "Most Popular",
  included: ["Diagnosis & safety inspection", "Minor wiring fixes", "30-day warranty"],
  features: ["Licensed experts", "Genuine spare parts", "No hidden diagnostic charges"]
}""")

    add_subsection_header("10.2", "Booking Entity Schema & LocalStorage Persistence (src/utils/bookingStorage.js)")
    add_body_paragraph("Appointments are dynamically instantiated and stored under the 'serviqBookings' LocalStorage key:")
    add_code_block("""{
  id: 15376,                                 // Auto-generated 5-digit unique ID
  serviceId: 1,                              // Foreign key to servicesData
  serviceName: "Professional Electrician",
  icon: "⚡",
  image: electricianImg,                     // Direct image link for thumbnail display
  date: "2026-09-18",
  time: "11:00 AM",
  status: "Confirmed",                       // "Confirmed" | "Completed" | "Cancelled"
  customerName: "Ajay M",
  customerPhone: "+91 9876543210",
  address: "Flat 204, Green Heights, Tech Zone",
  paymentMethod: "Cash after Service",
  price: 499,
  bookingDate: "2026-09-17"
}""")

    # ==========================================
    # 11. APPLICATION FLOW
    # ==========================================
    add_section_header("11.", "Application Flow")
    add_body_paragraph("The architectural runtime flow of the ServIQ platform illustrates how requests traverse the UI, routing, state managers, and persistence layers:")

    flow_diagram = """                [ Customer / User ]
                        │
                        ▼
                [ React Router DOM v6 ]
                        │
    ┌───────────────────┼───────────────────┐
    ▼                   ▼                   ▼
[ Home.jsx ]     [ Services.jsx ]   [ ServiceDetails.jsx ]
(Hero Search)     (Filter & Sort)    (Hero Banner & Gallery)
    │                   │                   │
    └───────────────────┴───────────────────┘
                        │
                        ▼
                [ Booking.jsx ]
        (Service Visual Spotlight Banner)
                        │
                        ▼
              [ BookingForm.jsx ]
      (Step 1: Date/Time Slot Selection)
      (Step 2: Customer Address & Phone)
      (Step 3: Payment Preference Choice)
                        │
                        ▼
            [ bookingStorage.js ]
      (Stores record in browser LocalStorage)
                        │
            ┌───────────┴───────────┐
            ▼                       ▼
   [ BookingSuccess.jsx ]    [ MyBookings.jsx ]
   (Official Receipt Card)   (Manage Appointments,
    #SRV-15376 Generated      Tabs: All/Confirmed,
                              Cancellation Modal)"""

    add_code_block(flow_diagram)

    # ==========================================
    # 12. SCREENSHOTS OF IMPORTANT MODULES
    # ==========================================
    add_section_header("12.", "Important Modules Screenshots & UI Walkthrough")
    add_body_paragraph(
        "Below are actual, high-resolution screenshots captured directly from the running ServIQ web application, showcasing the newly integrated real service photography, UI polish, and full booking flow:"
    )

    screenshots = [
        ("01_home_page.png", "Figure 1: ServIQ Home Page – Hero Section with Instant Search & Popular Services with Real Images"),
        ("02_all_services_catalog.png", "Figure 2: All Services Catalog Page – Category Filter Pills, Search Bar, and Service Cards"),
        ("03_service_details_electrician.png", "Figure 3: Service Details Page – Professional Electrician with Featured Hero Banner & Inclusions Checklist"),
        ("04_service_details_pest_control_gallery.png", "Figure 4: Service Details Page – Pest Control & Sanitization featuring Interactive Photo Gallery Switcher"),
        ("05_schedule_appointment_booking.png", "Figure 5: Schedule Appointment Page – Service Visual Spotlight Banner, Slot Picker & 3-Step Booking Form"),
        ("06_booking_confirmed_receipt.png", "Figure 6: Official Booking Confirmed Receipt – Unique Reference #SRV-15376 for Ajay M with Verified Details"),
        ("07_my_bookings_dashboard.png", "Figure 7: My Bookings Dashboard – Scheduled Appointments with Real Thumbnails, Status Badges & Cancellation Modal")
    ]

    for fname, caption in screenshots:
        fpath = os.path.join(SCREENSHOTS_DIR, fname)
        add_image_figure(fpath, caption)

    # ==========================================
    # 13. TESTING & VERIFICATION
    # ==========================================
    add_section_header("13.", "Testing & Verification")
    add_body_paragraph("Comprehensive manual and functional verification tests were performed across all core modules:")

    test_table = doc.add_table(rows=1, cols=5)
    test_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    test_table.autofit = False

    t_hdrs = ["Test Case", "Module Tested", "Input Data", "Expected Result", "Status"]
    for i, h in enumerate(t_hdrs):
        cell = test_table.rows[0].cells[i]
        cell.width = [Inches(1.4), Inches(1.3), Inches(1.4), Inches(1.8), Inches(0.6)][i]
        set_cell_background(cell, "1E3A8A")
        set_cell_margins(cell, 100, 100, 100, 100)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "Calibri"
        r.font.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    test_cases = [
        ("TC-01", "Home Page", "Open http://localhost:5173", "Hero headline, search bar, and 6 service cards with real images render cleanly.", "PASS"),
        ("TC-02", "Category Filter", "Click 'Cleaning' pill", "Only 'Full Home Deep Cleaning' card is displayed in the grid.", "PASS"),
        ("TC-03", "Search Engine", "Type 'plumb' into search", "Master Plumber Service card displayed; non-matching services hidden.", "PASS"),
        ("TC-04", "Service Details", "Click 'Details' on Electrician", "Hero image banner loads, what's included and guarantees display, sticky sidebar active.", "PASS"),
        ("TC-05", "Interactive Gallery", "Click thumb 2 on Pest Control", "Active hero banner switches smoothly to second sanitization image.", "PASS"),
        ("TC-06", "Slot Selection", "Click '01:00 PM' slot button", "Selected slot highlights with blue border and updates order summary.", "PASS"),
        ("TC-07", "Form Validation", "Submit empty booking form", "Displays inline validation error: 'Please fill in your name, phone, and address.'", "PASS"),
        ("TC-08", "Booking Creation", "Name: Ajay M, Phone: 9876543210", "Booking saved into LocalStorage, redirects to /booking-success with ID #SRV-15376.", "PASS"),
        ("TC-09", "Receipt Display", "Open /booking-success?id=15376", "Receipt card displays verified badge, service photo, customer name, date, time & price.", "PASS"),
        ("TC-10", "Appointment Cancel", "Click 'Cancel' in My Bookings", "Modal prompts confirmation; on confirm, status updates to 'Cancelled'.", "PASS")
    ]

    for row_idx, (t_id, mod, inp, exp, stat) in enumerate(test_cases):
        row = test_table.add_row()
        bg_col = "F8FAFC" if row_idx % 2 == 0 else "FFFFFF"
        for col_idx, text in enumerate([t_id, mod, inp, exp, stat]):
            cell = row.cells[col_idx]
            cell.width = [Inches(1.4), Inches(1.3), Inches(1.4), Inches(1.8), Inches(0.6)][col_idx]
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, 80, 80, 100, 100)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.name = "Calibri"
            r.font.size = Pt(9.0)
            if col_idx == 0:
                r.font.bold = True
                r.font.color.rgb = primary_color
            elif col_idx == 4:
                r.font.bold = True
                r.font.color.rgb = RGBColor(22, 101, 52) # Dark green
            else:
                r.font.color.rgb = body_color

    # ==========================================
    # 14. ADVANTAGES & KEY HIGHLIGHTS
    # ==========================================
    add_section_header("14.", "Advantages & Key Highlights")
    add_bullet("Ultra-Clean & Intuitive UI/UX", "Streamlined, clutter-free design philosophy allowing users to book in under 60 seconds.")
    add_bullet("Upfront Fixed Pricing", "100% transparent rates eliminate customer anxiety over surprise diagnostic charges.")
    add_bullet("Zero-Friction Scheduling", "Customers can book without mandatory upfront card payments using 'Pay after Service'.")
    add_bullet("Authentic Visuals", "Real service photography fosters trust and sets clear expectations for homeowners.")
    add_bullet("Decoupled Architecture", "Modular React components and utility layers simplify maintenance and future feature additions.")
    add_bullet("High Performance", "Near-instantaneous client-side filtering and page switches powered by Vite and useMemo.")

    # ==========================================
    # 15. FUTURE ENHANCEMENTS
    # ==========================================
    add_section_header("15.", "Future Enhancements")
    add_body_paragraph("ServIQ has been architected to accommodate seamless future growth and feature expansion:")
    add_bullet("Payment Gateway Integration", "Direct integration with Razorpay / Stripe for online credit card, debit card, and UPI transactions.")
    add_bullet("SMS & WhatsApp Notifications", "Automated SMS alerts and WhatsApp appointment reminders via Twilio.")
    add_bullet("Real-Time GPS Technician Tracking", "Live map interface displaying technician transit status and estimated arrival time.")
    add_bullet("Admin & Technician Portal", "Dedicated portal for technicians to accept jobs, upload repair photos, and mark tasks completed.")
    add_bullet("Customer Reviews & Rating Submission", "Post-service feedback collection allowing customers to leave star ratings and reviews.")

    # ==========================================
    # 16. CONCLUSION
    # ==========================================
    add_section_header("16.", "Conclusion")
    add_body_paragraph(
        "The ServIQ On-Demand Doorstep Home & Electrical Services Booking Platform successfully demonstrates how React.js and modern frontend tooling can be leveraged to engineer a responsive, production-ready, and user-centric web application. By combining modular component architecture, centralized state handling, persistent local storage, and authentic high-resolution photography, ServIQ delivers a seamless, reliable, and aesthetically pleasing booking experience for homeowners."
    )
    add_body_paragraph(
        "This project showcases mastery of modern React paradigms—including component lifecycle management, hook optimization, declarative routing, and state persistence—establishing a robust foundation for full-scale commercial deployment."
    )

    output_path = os.path.join(DOC_DIR, "ServIQ_Project_Documentation.docx")
    doc.save(output_path)
    print(f"Document successfully created at: {output_path}")

if __name__ == "__main__":
    create_documentation()
