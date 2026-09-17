import os
import sys
import subprocess

DOC_DIR = r"d:\Fontend Projects\serviq"
SCREENSHOTS_DIR = os.path.join(DOC_DIR, "documentation_screenshots")

# Ensure python-pptx is installed
try:
    import pptx
except ImportError:
    print("Installing python-pptx...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-pptx"])
    import pptx

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette Definitions
    c_navy = RGBColor(15, 23, 42)       # Slate 900 / #0f172a
    c_blue = RGBColor(30, 58, 138)      # Blue 900 / #1e3a8a
    c_primary = RGBColor(37, 99, 235)   # Blue 600 / #2563eb
    c_cyan = RGBColor(14, 116, 144)     # Cyan 700 / #0e7490
    c_emerald = RGBColor(16, 185, 129)  # Emerald 500 / #10b981
    c_amber = RGBColor(245, 158, 11)    # Amber 500 / #f59e0b
    c_bg_light = RGBColor(248, 250, 252)# Slate 50 / #f8fafc
    c_card_bg = RGBColor(255, 255, 255) # Pure White
    c_card_border = RGBColor(226, 232, 240) # Slate 200
    c_text_main = RGBColor(15, 23, 42)  # Dark text
    c_text_muted = RGBColor(71, 85, 105)# Slate 600
    c_white = RGBColor(255, 255, 255)

    def add_header(slide, title, category="SERVIQ – REACT.JS PROJECT PRESENTATION"):
        # Top banner background
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = c_navy
        top_bar.line.fill.background()

        # Accent thin stripe
        stripe = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(1.15), Inches(13.333), Inches(0.06))
        stripe.fill.solid()
        stripe.fill.fore_color.rgb = c_primary
        stripe.line.fill.background()

        # Category text
        txBox1 = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.5), Inches(0.3))
        tf1 = txBox1.text_frame
        tf1.word_wrap = True
        p1 = tf1.paragraphs[0]
        p1.text = category.upper()
        p1.font.name = "Arial"
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = c_cyan

        # Title text
        txBox2 = slide.shapes.add_textbox(Inches(0.8), Inches(0.40), Inches(11.5), Inches(0.6))
        tf2 = txBox2.text_frame
        tf2.word_wrap = True
        p2 = tf2.paragraphs[0]
        p2.text = title
        p2.font.name = "Arial"
        p2.font.size = Pt(22)
        p2.font.bold = True
        p2.font.color.rgb = c_white

        # Slide footer
        footer_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.02))
        footer_line.fill.solid()
        footer_line.fill.fore_color.rgb = c_card_border
        footer_line.line.fill.background()

        tx_footer = slide.shapes.add_textbox(Inches(0.8), Inches(7.1), Inches(11.733), Inches(0.3))
        tf_f = tx_footer.text_frame
        pf = tf_f.paragraphs[0]
        pf.text = "ServIQ Web Application | Developed by Ajay M (Junior Software Developer) | React.js & Vite"
        pf.font.name = "Arial"
        pf.font.size = Pt(9.5)
        pf.font.color.rgb = c_text_muted

    def add_card(slide, left, top, width, height, bg_color=c_card_bg, border_color=c_card_border):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1.2)
        else:
            card.line.fill.background()
        return card

    # ==========================================
    # SLIDE 1: TITLE SLIDE (PREMIUM DARK THEME)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = c_navy
    bg1.line.fill.background()

    # Decorative geometric accent boxes
    accent1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.5), Inches(0.8), Inches(4.2), Inches(5.8))
    accent1.fill.solid()
    accent1.fill.fore_color.rgb = RGBColor(30, 41, 59) # Slate 800
    accent1.line.color.rgb = c_primary
    accent1.line.width = Pt(1.5)

    # Decorative inner preview inside accent box
    img1_path = os.path.join(SCREENSHOTS_DIR, "01_home_page.png")
    if os.path.exists(img1_path):
        s1.shapes.add_picture(img1_path, Inches(8.7), Inches(1.0), width=Inches(3.8))

    # Badge: Front-end Engineering Project
    tag_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.2), Inches(3.4), Inches(0.45))
    tag_box.fill.solid()
    tag_box.fill.fore_color.rgb = RGBColor(30, 58, 138) # Blue 900
    tag_box.line.color.rgb = c_primary
    tf_tag = tag_box.text_frame
    p_tag = tf_tag.paragraphs[0]
    p_tag.alignment = PP_ALIGN.CENTER
    p_tag.text = "⚡ REACT.JS & VITE WEB APPLICATION"
    p_tag.font.name = "Arial"
    p_tag.font.size = Pt(10)
    p_tag.font.bold = True
    p_tag.font.color.rgb = c_white

    # Title
    t_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(7.2), Inches(1.8))
    tf_t = t_box.text_frame
    tf_t.word_wrap = True
    pt = tf_t.paragraphs[0]
    pt.text = "ServIQ"
    pt.font.name = "Arial"
    pt.font.size = Pt(54)
    pt.font.bold = True
    pt.font.color.rgb = c_white

    pt_sub = tf_t.add_paragraph()
    pt_sub.text = "On-Demand Doorstep Home & Electrical Services Booking Platform"
    pt_sub.font.name = "Arial"
    pt_sub.font.size = Pt(20)
    pt_sub.font.bold = True
    pt_sub.font.color.rgb = RGBColor(56, 189, 248) # Sky 400

    # Project Description
    desc_box = s1.shapes.add_textbox(Inches(1.0), Inches(3.7), Inches(7.0), Inches(1.2))
    tf_desc = desc_box.text_frame
    tf_desc.word_wrap = True
    pd = tf_desc.paragraphs[0]
    pd.text = "A production-grade, highly responsive web application enabling seamless doorstep service exploration, transparent fixed pricing, interactive photo galleries, instant appointment scheduling, and persistent booking management."
    pd.font.name = "Arial"
    pd.font.size = Pt(12)
    pd.font.color.rgb = RGBColor(203, 213, 225) # Slate 300

    # Author Credentials Card
    author_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(5.1), Inches(6.8), Inches(1.5))
    author_card.fill.solid()
    author_card.fill.fore_color.rgb = RGBColor(30, 41, 59)
    author_card.line.color.rgb = c_primary

    tf_auth = author_card.text_frame
    tf_auth.word_wrap = True
    p_a1 = tf_auth.paragraphs[0]
    p_a1.text = "👨‍💻 Project Developer: Ajay M"
    p_a1.font.name = "Arial"
    p_a1.font.size = Pt(14)
    p_a1.font.bold = True
    p_a1.font.color.rgb = c_white

    p_a2 = tf_auth.add_paragraph()
    p_a2.text = "Role: Junior Software Developer | Specialty: React.js & Modern Frontend Engineering"
    p_a2.font.name = "Arial"
    p_a2.font.size = Pt(11)
    p_a2.font.color.rgb = RGBColor(148, 163, 184)

    p_a3 = tf_auth.add_paragraph()
    p_a3.text = "Tech Stack: React.js (v19) • Vite • JavaScript (ES6+) • CSS3 • React Router v6 • LocalStorage"
    p_a3.font.name = "Arial"
    p_a3.font.size = Pt(10.5)
    p_a3.font.color.rgb = c_emerald

    # ==========================================
    # SLIDE 2: EXECUTIVE SUMMARY & PROBLEM STATEMENT
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Executive Summary & Problem Statement")

    # Left Card: The Problem
    add_card(s2, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    p_head = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(0.6))
    p_head.fill.solid()
    p_head.fill.fore_color.rgb = RGBColor(225, 29, 72) # Rose red
    p_head.line.fill.background()
    tf_ph = p_head.text_frame
    p_ph = tf_ph.paragraphs[0]
    p_ph.text = "⚠️ THE INDUSTRY PROBLEM"
    p_ph.font.name = "Arial"
    p_ph.font.size = Pt(13)
    p_ph.font.bold = True
    p_ph.font.color.rgb = c_white

    tb_prob = s2.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.3))
    tf_p = tb_prob.text_frame
    tf_p.word_wrap = True
    prob_points = [
        ("Hidden & Unpredictable Pricing", "Customers face surprise diagnostic inspection fees and fluctuating labor estimates without standard baselines."),
        ("Unverified Technicians", "Lack of safety assurances, background verification, or quality checks for doorstep handymen."),
        ("Friction in Scheduling", "Traditional booking requires repeated phone calls, manual coordination, and indefinite waiting times."),
        ("No Post-Service Warranty", "Zero accountability if an electrical or plumbing repair malfunctions shortly after completion.")
    ]
    for i, (title, desc) in enumerate(prob_points):
        p = tf_p.paragraphs[0] if i == 0 else tf_p.add_paragraph()
        p.text = f"• {title}: "
        p.font.name = "Arial"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = c_text_main
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = c_text_muted
        p.space_after = Pt(10)

    # Right Card: The ServIQ Solution
    add_card(s2, Inches(6.9), Inches(1.5), Inches(5.6), Inches(5.2))
    s_head = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.9), Inches(1.5), Inches(5.6), Inches(0.6))
    s_head.fill.solid()
    s_head.fill.fore_color.rgb = c_primary
    s_head.line.fill.background()
    tf_sh = s_head.text_frame
    p_sh = tf_sh.paragraphs[0]
    p_sh.text = "✨ THE SERVIQ DIGITAL SOLUTION"
    p_sh.font.name = "Arial"
    p_sh.font.size = Pt(13)
    p_sh.font.bold = True
    p_sh.font.color.rgb = c_white

    tb_sol = s2.shapes.add_textbox(Inches(7.1), Inches(2.2), Inches(5.2), Inches(4.3))
    tf_s = tb_sol.text_frame
    tf_s.word_wrap = True
    sol_points = [
        ("100% Upfront Fixed Pricing", "Standardized rates (e.g. ₹399 - ₹2,499) displayed upfront with complete checklists of inclusions."),
        ("Certified & Background-Checked Experts", "Every service is serviced by verified, trained professionals with authentic identity verification."),
        ("Instant 3-Step Scheduling", "Pick a preferred 2-hour slot (09:00 AM to 07:00 PM), input address, and confirm in under 60 seconds."),
        ("Pay After Service & 30-Day Guarantee", "Customers can pay via cash or UPI after satisfactory job completion, backed by a 30-day rework warranty.")
    ]
    for i, (title, desc) in enumerate(sol_points):
        p = tf_s.paragraphs[0] if i == 0 else tf_s.add_paragraph()
        p.text = f"• {title}: "
        p.font.name = "Arial"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = c_text_main
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = c_text_muted
        p.space_after = Pt(10)

    # ==========================================
    # SLIDE 3: OBJECTIVES & SCOPE
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Project Objectives & Technical Scope")

    objectives_data = [
        ("01", "Modular Component Architecture", "Build cleanly decoupled, reusable React components (ServiceCard, ServiceList, BookingForm, NavBar, Footer, Button) adhering to standard separation of concerns."),
        ("02", "Centralized State Management", "Leverage React Hooks (useState, useEffect, useMemo) and React Context API to achieve responsive client-side state without external state bloat."),
        ("03", "Persistent Client Storage Layer", "Establish synchronous, zero-latency local storage mechanisms utilizing LocalStorage for booking schedules, status transitions, and user profile data."),
        ("04", "Rich Visual Media Experience", "Integrate high-definition photography across all service cards and provide interactive multi-view photo galleries for specialized services."),
        ("05", "Dynamic Multi-Criteria Filtering", "Implement instantaneous client-side keyword search, 8-category filter pills, and multi-tier sorting (rating, price, recommendation)."),
        ("06", "Responsive Production Standard", "Ensure seamless layout adaptation across mobile viewports, tablets, laptops, and ultra-wide desktop monitors with fluid CSS styling.")
    ]

    for idx, (num, title, desc) in enumerate(objectives_data):
        row = idx // 2
        col = idx % 2
        l = Inches(0.8 + col * 6.0)
        t = Inches(1.5 + row * 1.75)
        add_card(s3, l, t, Inches(5.7), Inches(1.55))

        # Number circle badge
        badge = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, l + Inches(0.2), t + Inches(0.2), Inches(0.65), Inches(0.65))
        badge.fill.solid()
        badge.fill.fore_color.rgb = c_primary if idx % 2 == 0 else c_cyan
        badge.line.fill.background()
        tf_b = badge.text_frame
        p_b = tf_b.paragraphs[0]
        p_b.alignment = PP_ALIGN.CENTER
        p_b.text = num
        p_b.font.name = "Arial"
        p_b.font.size = Pt(13)
        p_b.font.bold = True
        p_b.font.color.rgb = c_white

        # Text
        tx = s3.shapes.add_textbox(l + Inches(1.0), t + Inches(0.12), Inches(4.5), Inches(1.3))
        tf = tx.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = "Arial"
        p_t.font.size = Pt(12)
        p_t.font.bold = True
        p_t.font.color.rgb = c_text_main

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = "Arial"
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = c_text_muted

    # ==========================================
    # SLIDE 4: TECHNOLOGY STACK & ARCHITECTURE
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Technology Stack & Core Dependencies")

    tech_cards = [
        ("React.js (v19)", "Frontend Library", "Provides component lifecycle hooks, dynamic Virtual DOM updates, and declarative UI rendering.", c_primary),
        ("Vite (v6)", "Build Tooling", "Delivers ultra-fast Hot Module Replacement (HMR) and optimized ES-module bundling for production.", c_cyan),
        ("React Router (v6)", "Client-Side Routing", "Manages declarative browser history routing, parameterized URLs (/services/:id), and deep-linking.", c_blue),
        ("CSS3 Design System", "Styling & UI Tokens", "Custom responsive flexbox/grid layouts, CSS variables, glassmorphism overlays, and micro-transitions.", c_emerald),
        ("Context API", "Global State", "Coordinates user authentication sessions, logged-in customer data, and global state propagation.", c_amber),
        ("LocalStorage API", "Persistence Layer", "Guarantees offline-capable, client-side data persistence for scheduled appointments and bookings.", c_navy)
    ]

    for idx, (name, role, details, color) in enumerate(tech_cards):
        row = idx // 3
        col = idx % 3
        l = Inches(0.8 + col * 4.0)
        t = Inches(1.5 + row * 2.6)
        card = add_card(s4, l, t, Inches(3.7), Inches(2.3))

        # Colored header bar
        bar = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, Inches(3.7), Inches(0.4))
        bar.fill.solid()
        bar.fill.fore_color.rgb = color
        bar.line.fill.background()

        tf_bar = bar.text_frame
        p_bar = tf_bar.paragraphs[0]
        p_bar.text = role.upper()
        p_bar.font.name = "Arial"
        p_bar.font.size = Pt(9.5)
        p_bar.font.bold = True
        p_bar.font.color.rgb = c_white

        tx = s4.shapes.add_textbox(l + Inches(0.2), t + Inches(0.5), Inches(3.3), Inches(1.7))
        tf = tx.text_frame
        tf.word_wrap = True
        p_name = tf.paragraphs[0]
        p_name.text = name
        p_name.font.name = "Arial"
        p_name.font.size = Pt(14)
        p_name.font.bold = True
        p_name.font.color.rgb = c_text_main
        p_name.space_after = Pt(4)

        p_det = tf.add_paragraph()
        p_det.text = details
        p_det.font.name = "Arial"
        p_det.font.size = Pt(10)
        p_det.font.color.rgb = c_text_muted

    # ==========================================
    # SLIDE 5: SYSTEM ARCHITECTURE & DATA FLOW
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "System Architecture & End-to-End Data Flow")

    # 4 Architecture Flow Steps in horizontal chain
    steps = [
        ("Step 1: Presentation Layer", "React UI Components", "• Navbar & Footer\n• ServiceCard with images\n• ServiceList grid\n• BookingForm (3-Step)\n• Modal Dialogs", c_primary),
        ("Step 2: Routing & Context", "React Router & AuthContext", "• Dynamic paths (/book/:id)\n• URL Query parsing (?cat=&q=)\n• Global User Session\n• Auth state propagation", c_cyan),
        ("Step 3: Business Logic", "Services Data & Hooks", "• 8 Service Catalog definitions\n• useMemo search/filter\n• Gallery image switcher\n• Slot selection validation", c_emerald),
        ("Step 4: Persistence Layer", "LocalStorage Booking Engine", "• addBooking() with ID generation\n• getStoredBookings()\n• cancelBookingById()\n• Synchronous read/write", c_navy)
    ]

    for idx, (title, sub, bullets, col_accent) in enumerate(steps):
        l = Inches(0.8 + idx * 3.0)
        t = Inches(1.6)
        w = Inches(2.7)
        h = Inches(4.5)

        card = add_card(s5, l, t, w, h)
        # Top banner
        top = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, w, Inches(0.7))
        top.fill.solid()
        top.fill.fore_color.rgb = col_accent
        top.line.fill.background()

        tf_top = top.text_frame
        p_t1 = tf_top.paragraphs[0]
        p_t1.text = title
        p_t1.font.name = "Arial"
        p_t1.font.size = Pt(10)
        p_t1.font.bold = True
        p_t1.font.color.rgb = c_white

        tx = s5.shapes.add_textbox(l + Inches(0.15), t + Inches(0.8), Inches(2.4), Inches(3.5))
        tf = tx.text_frame
        tf.word_wrap = True

        p_sub = tf.paragraphs[0]
        p_sub.text = sub
        p_sub.font.name = "Arial"
        p_sub.font.size = Pt(11.5)
        p_sub.font.bold = True
        p_sub.font.color.rgb = c_text_main
        p_sub.space_after = Pt(8)

        p_b = tf.add_paragraph()
        p_b.text = bullets
        p_b.font.name = "Arial"
        p_b.font.size = Pt(10)
        p_b.font.color.rgb = c_text_muted

        # Arrow icon between cards
        if idx < 3:
            arrow = s5.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, l + Inches(2.75), t + Inches(2.2), Inches(0.2), Inches(0.3))
            arrow.fill.solid()
            arrow.fill.fore_color.rgb = c_primary
            arrow.line.fill.background()

    # Flow summary note
    note = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.6))
    note.fill.solid()
    note.fill.fore_color.rgb = RGBColor(241, 245, 249)
    note.line.color.rgb = c_primary
    tf_n = note.text_frame
    pn = tf_n.paragraphs[0]
    pn.text = "🔄 Clean Unidirectional Data Flow: User interaction triggers hook state changes → computed via useMemo → persisted to LocalStorage → real-time UI synchronization."
    pn.font.name = "Arial"
    pn.font.size = Pt(10.5)
    pn.font.bold = True
    pn.font.color.rgb = c_navy

    # ==========================================
    # SLIDE 6: MODULE 1 – HOME & HERO MODULE
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Module 1: Landing Gateway & Popular Services Showcase")

    # Left: Explanation & Architecture
    add_card(s6, Inches(0.8), Inches(1.5), Inches(5.2), Inches(5.2))
    tx6 = s6.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.8), Inches(4.8))
    tf6 = tx6.text_frame
    tf6.word_wrap = True

    p_h = tf6.paragraphs[0]
    p_h.text = "Key Components & Features:"
    p_h.font.name = "Arial"
    p_h.font.size = Pt(14)
    p_h.font.bold = True
    p_h.font.color.rgb = c_blue
    p_h.space_after = Pt(8)

    h_bullets = [
        ("Hero Headline & Search Bar", "Intuitive search bar with instant keyword routing to the service discovery engine."),
        ("Quick Category Filter Pills", "Direct one-click filters for Electrical, Plumbing, Cleaning, AC & Appliances, and Pest Control."),
        ("Authentic Service Photography", "Six featured services rendered with real photographic banners, prices, and star ratings."),
        ("Hover Micro-Interactions", "Cards feature smooth CSS scale-zoom effects (transform: scale(1.06)) and glassmorphic badge overlays."),
        ("Value Proposition & Workflow", "3-Step 'How It Works' guide and homeowner trust highlights (30-day warranty, verified pros).")
    ]
    for title, desc in h_bullets:
        p = tf6.add_paragraph()
        p.text = f"• {title}: "
        p.font.name = "Arial"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = c_text_main
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = c_text_muted
        p.space_after = Pt(6)

    # Right: Screenshot Frame
    add_card(s6, Inches(6.3), Inches(1.5), Inches(6.2), Inches(5.2))
    img_h = os.path.join(SCREENSHOTS_DIR, "01_home_page.png")
    if os.path.exists(img_h):
        s6.shapes.add_picture(img_h, Inches(6.45), Inches(1.65), width=Inches(5.9))
        tx_cap = s6.shapes.add_textbox(Inches(6.45), Inches(6.3), Inches(5.9), Inches(0.3))
        tf_c = tx_cap.text_frame
        pc = tf_c.paragraphs[0]
        pc.alignment = PP_ALIGN.CENTER
        pc.text = "Figure 1: Home Landing Page – Hero Section & Real Service Card Banners"
        pc.font.name = "Arial"
        pc.font.size = Pt(9.5)
        pc.font.italic = True
        pc.font.color.rgb = c_text_muted

    # ==========================================
    # SLIDE 7: MODULE 2 – ALL SERVICES CATALOG & FILTERING
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Module 2: Service Catalog Discovery, Search & Sorting")

    # Left: Explanation
    add_card(s7, Inches(0.8), Inches(1.5), Inches(5.2), Inches(5.2))
    tx7 = s7.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.8), Inches(4.8))
    tf7 = tx7.text_frame
    tf7.word_wrap = True

    p_h7 = tf7.paragraphs[0]
    p_h7.text = "Dynamic Catalog Capabilities:"
    p_h7.font.name = "Arial"
    p_h7.font.size = Pt(14)
    p_h7.font.bold = True
    p_h7.font.color.rgb = c_blue
    p_h7.space_after = Pt(8)

    cat_bullets = [
        ("8 Domestic Categories", "Pills for All, Electrical, Plumbing, AC & Appliances, Cleaning, Pest Control, Painting, and Carpentry."),
        ("Real-Time Filter Engine", "Instant search filtered across service names, detailed descriptions, and categories."),
        ("Multi-Tiered Sorting", "Sort services dynamically by Recommended, Highest Rated, Price: Low-to-High, and Price: High-to-Low."),
        ("Performance with useMemo", "Prevents unnecessary array re-filtering on unrelated parent re-renders."),
        ("Empty State Handling", "Displays clear feedback and a single-click 'Clear Filters' button when zero matches exist.")
    ]
    for title, desc in cat_bullets:
        p = tf7.add_paragraph()
        p.text = f"• {title}: "
        p.font.name = "Arial"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = c_text_main
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = c_text_muted
        p.space_after = Pt(6)

    # Right: Screenshot Frame
    add_card(s7, Inches(6.3), Inches(1.5), Inches(6.2), Inches(5.2))
    img_cat = os.path.join(SCREENSHOTS_DIR, "02_all_services_catalog.png")
    if os.path.exists(img_cat):
        s7.shapes.add_picture(img_cat, Inches(6.45), Inches(1.65), width=Inches(5.9))
        tx_cap = s7.shapes.add_textbox(Inches(6.45), Inches(6.3), Inches(5.9), Inches(0.3))
        tf_c = tx_cap.text_frame
        pc = tf_c.paragraphs[0]
        pc.alignment = PP_ALIGN.CENTER
        pc.text = "Figure 2: All Services Catalog – Filter Pills, Search Bar, and Service Grid"
        pc.font.name = "Arial"
        pc.font.size = Pt(9.5)
        pc.font.italic = True
        pc.font.color.rgb = c_text_muted

    # ==========================================
    # SLIDE 8: MODULE 3 – SERVICE DETAILS & PHOTO GALLERY
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Module 3: Service Details & Interactive Multi-Photo Gallery")

    # Left: Explanation
    add_card(s8, Inches(0.8), Inches(1.5), Inches(4.5), Inches(5.2))
    tx8 = s8.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.1), Inches(4.8))
    tf8 = tx8.text_frame
    tf8.word_wrap = True

    p_h8 = tf8.paragraphs[0]
    p_h8.text = "Deep Service Inspector:"
    p_h8.font.name = "Arial"
    p_h8.font.size = Pt(13)
    p_h8.font.bold = True
    p_h8.font.color.rgb = c_blue
    p_h8.space_after = Pt(6)

    det_bullets = [
        ("Full-Bleed Hero Banner", "High-resolution 340px photographic banner with floating category and quality badge tags."),
        ("Interactive Gallery Switcher", "For services with multiple photographs (e.g. Pest Control & Sanitization), users can toggle between angles."),
        ("What's Included Checklist", "Complete transparency on diagnostic, labor, inspection, and post-service cleanup."),
        ("ServIQ Service Promise", "Highlights verified technician safety, transparent genuine spares, and 30-day warranty."),
        ("Sticky Booking Box", "Right sidebar remains sticky during scroll with direct time-slot booking CTA.")
    ]
    for title, desc in det_bullets:
        p = tf8.add_paragraph()
        p.text = f"• {title}: "
        p.font.name = "Arial"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = c_text_main
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = c_text_muted
        p.space_after = Pt(4)

    # Right: 2 Screenshots (Electrician details + Pest Control Gallery)
    add_card(s8, Inches(5.6), Inches(1.5), Inches(6.9), Inches(5.2))
    img_elec = os.path.join(SCREENSHOTS_DIR, "03_service_details_electrician.png")
    img_pest = os.path.join(SCREENSHOTS_DIR, "04_service_details_pest_control_gallery.png")

    if os.path.exists(img_elec) and os.path.exists(img_pest):
        s8.shapes.add_picture(img_elec, Inches(5.75), Inches(1.65), width=Inches(3.2))
        s8.shapes.add_picture(img_pest, Inches(9.15), Inches(1.65), width=Inches(3.2))

        tx_cap = s8.shapes.add_textbox(Inches(5.6), Inches(6.3), Inches(6.9), Inches(0.3))
        tf_c = tx_cap.text_frame
        pc = tf_c.paragraphs[0]
        pc.alignment = PP_ALIGN.CENTER
        pc.text = "Figures 3 & 4: Left – Electrician Details with Inclusions | Right – Pest Control Multi-Photo Gallery"
        pc.font.name = "Arial"
        pc.font.size = Pt(9.5)
        pc.font.italic = True
        pc.font.color.rgb = c_text_muted

    # ==========================================
    # SLIDE 9: MODULE 4 – 3-STEP APPOINTMENT SCHEDULING
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Module 4: 3-Step Hassle-Free Appointment Booking Flow")

    # Left: Explanation
    add_card(s9, Inches(0.8), Inches(1.5), Inches(5.2), Inches(5.2))
    tx9 = s9.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.8), Inches(4.8))
    tf9 = tx9.text_frame
    tf9.word_wrap = True

    p_h9 = tf9.paragraphs[0]
    p_h9.text = "Booking Engineering Highlights:"
    p_h9.font.name = "Arial"
    p_h9.font.size = Pt(14)
    p_h9.font.bold = True
    p_h9.font.color.rgb = c_blue
    p_h9.space_after = Pt(8)

    book_bullets = [
        ("Visual Service Spotlight", "Top banner previews selected service image, category, duration, rating, and upfront charge."),
        ("Service Switcher Dropdown", "Customers can switch services on the fly without navigating away from the scheduling screen."),
        ("Step 1: Date & Slot Selection", "Restricts past date selection; provides 6 daily 2-hour slots (09:00 AM to 07:00 PM)."),
        ("Step 2: Customer Address & Phone", "Captures customer name, mobile contact, street address, and optional landmark (auto-filled if logged in)."),
        ("Step 3: Flexible Payment Preference", "Choice between '💵 Pay after Service' and '💳 Pay Online'."),
        ("Real-Time Order Summary", "Dynamic sidebar confirms booked thumbnail, date, time slot, and total amount payable.")
    ]
    for title, desc in book_bullets:
        p = tf9.add_paragraph()
        p.text = f"• {title}: "
        p.font.name = "Arial"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = c_text_main
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = c_text_muted
        p.space_after = Pt(5)

    # Right: Screenshot Frame
    add_card(s9, Inches(6.3), Inches(1.5), Inches(6.2), Inches(5.2))
    img_book = os.path.join(SCREENSHOTS_DIR, "05_schedule_appointment_booking.png")
    if os.path.exists(img_book):
        s9.shapes.add_picture(img_book, Inches(6.45), Inches(1.65), width=Inches(5.9))
        tx_cap = s9.shapes.add_textbox(Inches(6.45), Inches(6.3), Inches(5.9), Inches(0.3))
        tf_c = tx_cap.text_frame
        pc = tf_c.paragraphs[0]
        pc.alignment = PP_ALIGN.CENTER
        pc.text = "Figure 5: Schedule Appointment Page – Spotlight Card, Slot Picker & 3-Step Form"
        pc.font.name = "Arial"
        pc.font.size = Pt(9.5)
        pc.font.italic = True
        pc.font.color.rgb = c_text_muted

    # ==========================================
    # SLIDE 10: MODULE 5 – BOOKING RECEIPT CONFIRMATION
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Module 5: Official Booking Confirmation & Receipt Generation")

    # Left: Explanation
    add_card(s10, Inches(0.8), Inches(1.5), Inches(5.2), Inches(5.2))
    tx10 = s10.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.8), Inches(4.8))
    tf10 = tx10.text_frame
    tf10.word_wrap = True

    p_h10 = tf10.paragraphs[0]
    p_h10.text = "Receipt Confirmation Highlights:"
    p_h10.font.name = "Arial"
    p_h10.font.size = Pt(14)
    p_h10.font.bold = True
    p_h10.font.color.rgb = c_blue
    p_h10.space_after = Pt(8)

    rec_bullets = [
        ("Auto-Generated Booking Reference", "Generates unique tracking identifier (e.g. #SRV-15376) for technician coordination."),
        ("Verified Technician Assignment", "Assures customer that a certified technician has been reserved for their specific slot."),
        ("Itemized Service Breakdown", "Displays thumbnail photo of booked service, schedule date/time, customer name, and exact price."),
        ("Location Verification", "Confirms destination address with optional landmark."),
        ("Seamless Post-Booking Actions", "Direct CTA buttons to 'View in My Bookings', 'Book Another Service', or navigate back Home.")
    ]
    for title, desc in rec_bullets:
        p = tf10.add_paragraph()
        p.text = f"• {title}: "
        p.font.name = "Arial"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = c_text_main
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = c_text_muted
        p.space_after = Pt(6)

    # Right: Screenshot Frame
    add_card(s10, Inches(6.3), Inches(1.5), Inches(6.2), Inches(5.2))
    img_rec = os.path.join(SCREENSHOTS_DIR, "06_booking_confirmed_receipt.png")
    if os.path.exists(img_rec):
        s10.shapes.add_picture(img_rec, Inches(6.45), Inches(1.65), width=Inches(5.9))
        tx_cap = s10.shapes.add_textbox(Inches(6.45), Inches(6.3), Inches(5.9), Inches(0.3))
        tf_c = tx_cap.text_frame
        pc = tf_c.paragraphs[0]
        pc.alignment = PP_ALIGN.CENTER
        pc.text = "Figure 6: Official Booking Confirmed Receipt – Unique Reference #SRV-15376 for Ajay M"
        pc.font.name = "Arial"
        pc.font.size = Pt(9.5)
        pc.font.italic = True
        pc.font.color.rgb = c_text_muted

    # ==========================================
    # SLIDE 11: MODULE 6 – MY BOOKINGS MANAGEMENT DASHBOARD
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Module 6: Appointment Dashboard & Booking Lifecycle")

    # Left: Explanation
    add_card(s11, Inches(0.8), Inches(1.5), Inches(5.2), Inches(5.2))
    tx11 = s11.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.8), Inches(4.8))
    tf11 = tx11.text_frame
    tf11.word_wrap = True

    p_h11 = tf11.paragraphs[0]
    p_h11.text = "Management Dashboard Features:"
    p_h11.font.name = "Arial"
    p_h11.font.size = Pt(14)
    p_h11.font.bold = True
    p_h11.font.color.rgb = c_blue
    p_h11.space_after = Pt(8)

    dash_bullets = [
        ("Interactive Status Tabs", "Filter appointments by All, Confirmed, Completed, or Cancelled with dynamic count badges."),
        ("Rich Photographic Cards", "Each appointment card displays the corresponding service's photo thumbnail, booking ID, address, date, and price."),
        ("Two-Step Cancellation Modal", "Active confirmed bookings can be cancelled with a confirmation modal, avoiding accidental clicks."),
        ("Immediate State Synchronization", "Cancelling an appointment updates LocalStorage and re-renders the dashboard instantly with zero page reload."),
        ("Re-booking Shortcut", "Completed or cancelled bookings feature a 'Book Again' button directing back to the scheduling page.")
    ]
    for title, desc in dash_bullets:
        p = tf11.add_paragraph()
        p.text = f"• {title}: "
        p.font.name = "Arial"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = c_text_main
        run = p.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = c_text_muted
        p.space_after = Pt(6)

    # Right: Screenshot Frame
    add_card(s11, Inches(6.3), Inches(1.5), Inches(6.2), Inches(5.2))
    img_dash = os.path.join(SCREENSHOTS_DIR, "07_my_bookings_dashboard.png")
    if os.path.exists(img_dash):
        s11.shapes.add_picture(img_dash, Inches(6.45), Inches(1.65), width=Inches(5.9))
        tx_cap = s11.shapes.add_textbox(Inches(6.45), Inches(6.3), Inches(5.9), Inches(0.3))
        tf_c = tx_cap.text_frame
        pc = tf_c.paragraphs[0]
        pc.alignment = PP_ALIGN.CENTER
        pc.text = "Figure 7: My Bookings Dashboard – Status Tabs, Real Thumbnails & Cancellation Controls"
        pc.font.name = "Arial"
        pc.font.size = Pt(9.5)
        pc.font.italic = True
        pc.font.color.rgb = c_text_muted

    # ==========================================
    # SLIDE 12: CORE REACT CONCEPTS DEMONSTRATED
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "Core React Concepts Implemented in ServIQ")

    react_concepts = [
        ("Functional Components & Props", "Components like ServiceCard receive typed data objects, separating data from presentation.", "const ServiceCard = ({ service }) => { ... }"),
        ("Interactive State (useState)", "Manages user search queries, active category tabs, gallery thumbnails, and form inputs.", "const [activeImage, setActiveImage] = useState(service?.image);"),
        ("Performance (useMemo)", "Memoizes filtered & sorted service arrays to prevent expensive recalculations.", "const filteredServices = useMemo(() => { ... }, [cat, search, sort]);"),
        ("Side Effects (useEffect)", "Synchronizes LocalStorage data on mount and updates customer details on user login.", "useEffect(() => { setBookings(getStoredBookings()); }, []);"),
        ("Global Context (useContext)", "Shares authentication state, user credentials, and logout dispatch globally.", "const { currentUser } = useAuth();"),
        ("Conditional Rendering", "Dynamically renders multi-photo gallery thumbs, status badges, and empty search results.", "{gallery.length > 1 && <GalleryThumbs images={gallery} />}")
    ]

    for idx, (title, desc, code) in enumerate(react_concepts):
        row = idx // 2
        col = idx % 2
        l = Inches(0.8 + col * 6.0)
        t = Inches(1.5 + row * 1.75)
        add_card(s12, l, t, Inches(5.7), Inches(1.55))

        tx = s12.shapes.add_textbox(l + Inches(0.2), t + Inches(0.12), Inches(5.3), Inches(1.35))
        tf = tx.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = f"⚛️ {title}"
        p_t.font.name = "Arial"
        p_t.font.size = Pt(11.5)
        p_t.font.bold = True
        p_t.font.color.rgb = c_primary

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = "Arial"
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = c_text_muted

        p_c = tf.add_paragraph()
        p_c.text = code
        p_c.font.name = "Consolas"
        p_c.font.size = Pt(9)
        p_c.font.color.rgb = RGBColor(15, 23, 42)

    # ==========================================
    # SLIDE 13: TESTING & QUALITY VERIFICATION
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "Quality Assurance & Test Verification Matrix")

    # Table of Test Cases
    table_shape = s13.shapes.add_table(rows=8, cols=5, left=Inches(0.8), top=Inches(1.5), width=Inches(11.733), height=Inches(5.0))
    table = table_shape.table

    # Column widths
    table.columns[0].width = Inches(1.2) # ID
    table.columns[1].width = Inches(2.3) # Module
    table.columns[2].width = Inches(3.2) # Input
    table.columns[3].width = Inches(3.8) # Expected Result
    table.columns[4].width = Inches(1.233) # Status

    headers = ["Test ID", "Target Module", "Test Input / Action", "Expected Outcome", "Status"]
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = c_navy
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = "Arial"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = c_white

    test_matrix = [
        ("TC-01", "Home Landing Page", "Visit http://localhost:5173", "Hero banner, search bar, and 6 service cards with real images render cleanly.", "PASS"),
        ("TC-02", "Category Filter", "Select 'Cleaning' pill", "Grid filters to show only 'Full Home Deep Cleaning' card.", "PASS"),
        ("TC-03", "Keyword Search", "Type 'plumb' in search bar", "Instantly filters to Master Plumber Service; non-matching hidden.", "PASS"),
        ("TC-04", "Service Details", "Click 'Details' on Electrician", "Renders 340px hero banner, what's included list, and sticky price box.", "PASS"),
        ("TC-05", "Interactive Gallery", "Click thumb 2 on Pest Control", "Active hero banner switches smoothly to second sanitization image.", "PASS"),
        ("TC-06", "Slot Booking Form", "Select date & '11:00 AM' slot", "Highlights selected slot in blue, updates right-hand order summary.", "PASS"),
        ("TC-07", "Receipt & Persistence", "Confirm booking for Ajay M", "Saved to LocalStorage, redirects to receipt with ID #SRV-15376.", "PASS")
    ]

    for row_idx, (t_id, mod, inp, exp, stat) in enumerate(test_matrix, start=1):
        bg = RGBColor(248, 250, 252) if row_idx % 2 == 0 else RGBColor(255, 255, 255)
        for col_idx, val in enumerate([t_id, mod, inp, exp, stat]):
            cell = table.cell(row_idx, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = "Arial"
            p.font.size = Pt(9.5)
            if col_idx == 0:
                p.font.bold = True
                p.font.color.rgb = c_primary
            elif col_idx == 4:
                p.font.bold = True
                p.font.color.rgb = c_emerald
            else:
                p.font.color.rgb = c_text_main

    # ==========================================
    # SLIDE 14: KEY ADVANTAGES & BUSINESS IMPACT
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "Key Advantages & Platform Value")

    advantages = [
        ("⚡ 60-Second Booking Speed", "Frictionless scheduling workflow eliminates tedious back-and-forth phone coordination.", c_primary),
        ("🏷️ 100% Upfront Fixed Rates", "Eliminates diagnostic estimate anxiety by providing clear, fixed prices prior to technician dispatch.", c_cyan),
        ("🛡️ Safety & 30-Day Guarantee", "Background-checked professionals backed by free re-servicing if unsatisfied within 30 days.", c_emerald),
        ("📸 Authentic Visual Experience", "Real photography gives customers confidence in the professional quality of doorstep services.", c_amber),
        ("💳 Zero Financial Risk", "'Pay After Service' allows customers to inspect repairs before releasing cash or UPI payment.", c_blue),
        ("📱 Universal Device Support", "Responsive layout functions flawlessly across smartphones, tablets, laptops, and wide monitors.", c_navy)
    ]

    for idx, (title, desc, color) in enumerate(advantages):
        row = idx // 2
        col = idx % 2
        l = Inches(0.8 + col * 6.0)
        t = Inches(1.5 + row * 1.75)
        card = add_card(s14, l, t, Inches(5.7), Inches(1.55))

        # Colored left vertical bar
        vbar = s14.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, Inches(0.12), Inches(1.55))
        vbar.fill.solid()
        vbar.fill.fore_color.rgb = color
        vbar.line.fill.background()

        tx = s14.shapes.add_textbox(l + Inches(0.3), t + Inches(0.15), Inches(5.2), Inches(1.3))
        tf = tx.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = "Arial"
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = c_text_main
        p_t.space_after = Pt(4)

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = "Arial"
        p_d.font.size = Pt(10.5)
        p_d.font.color.rgb = c_text_muted

    # ==========================================
    # SLIDE 15: FUTURE ROADMAP & SCALABILITY
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "Future Roadmap & Commercial Scalability")

    roadmap_steps = [
        ("Phase 1", "Payment Gateway Integration", "Direct integration with Razorpay and Stripe for automated credit/debit card checkout, netbanking, and UPI QR payments.", c_primary),
        ("Phase 2", "SMS & WhatsApp Notifications", "Automated real-time dispatch alerts and appointment reminders sent to customer mobile numbers via Twilio API.", c_cyan),
        ("Phase 3", "Live GPS Technician Tracking", "Interactive Leaflet / Google Maps interface displaying technician transit status and estimated arrival time (ETA).", c_emerald),
        ("Phase 4", "Technician Mobile Companion", "Dedicated portal for certified technicians to accept jobs, navigate to customer premises, and upload job completion photos.", c_amber),
        ("Phase 5", "Ratings & Photo Reviews", "Community review submission enabling customers to post photo proof and 5-star ratings post service.", c_blue)
    ]

    for idx, (phase, title, desc, color) in enumerate(roadmap_steps):
        t = Inches(1.5 + idx * 1.05)
        card = add_card(s15, Inches(0.8), t, Inches(11.733), Inches(0.9))

        # Phase tag
        ptag = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), t + Inches(0.18), Inches(1.3), Inches(0.52))
        ptag.fill.solid()
        ptag.fill.fore_color.rgb = color
        ptag.line.fill.background()
        tf_pt = ptag.text_frame
        p_pt = tf_pt.paragraphs[0]
        p_pt.alignment = PP_ALIGN.CENTER
        p_pt.text = phase
        p_pt.font.name = "Arial"
        p_pt.font.size = Pt(11)
        p_pt.font.bold = True
        p_pt.font.color.rgb = c_white

        # Title & Details
        tx = s15.shapes.add_textbox(Inches(2.5), t + Inches(0.1), Inches(9.8), Inches(0.7))
        tf = tx.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = title + " – "
        p_t.font.name = "Arial"
        p_t.font.size = Pt(12)
        p_t.font.bold = True
        p_t.font.color.rgb = c_text_main

        run = p_t.add_run()
        run.text = desc
        run.font.bold = False
        run.font.size = Pt(10.5)
        run.font.color.rgb = c_text_muted

    # ==========================================
    # SLIDE 16: CONCLUSION & Q&A
    # ==========================================
    s16 = prs.slides.add_slide(blank_layout)
    bg16 = s16.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg16.fill.solid()
    bg16.fill.fore_color.rgb = c_navy
    bg16.line.fill.background()

    # Center box
    center_box = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.8), Inches(1.2), Inches(9.733), Inches(5.1))
    center_box.fill.solid()
    center_box.fill.fore_color.rgb = RGBColor(30, 41, 59)
    center_box.line.color.rgb = c_primary
    center_box.line.width = Pt(1.5)

    tx16 = s16.shapes.add_textbox(Inches(2.2), Inches(1.6), Inches(8.9), Inches(4.3))
    tf16 = tx16.text_frame
    tf16.word_wrap = True

    p1 = tf16.paragraphs[0]
    p1.alignment = PP_ALIGN.CENTER
    p1.text = "Thank You!"
    p1.font.name = "Arial"
    p1.font.size = Pt(44)
    p1.font.bold = True
    p1.font.color.rgb = c_white
    p1.space_after = Pt(10)

    p2 = tf16.add_paragraph()
    p2.alignment = PP_ALIGN.CENTER
    p2.text = "ServIQ – Doorstep Home & Electrical Services Booking Platform"
    p2.font.name = "Arial"
    p2.font.size = Pt(18)
    p2.font.bold = True
    p2.font.color.rgb = RGBColor(56, 189, 248)
    p2.space_after = Pt(16)

    p3 = tf16.add_paragraph()
    p3.alignment = PP_ALIGN.CENTER
    p3.text = "A modern, reliable, and user-friendly digital solution developed with React.js, Vite, and modern Web engineering principles."
    p3.font.name = "Arial"
    p3.font.size = Pt(12)
    p3.font.color.rgb = RGBColor(203, 213, 225)
    p3.space_after = Pt(24)

    p4 = tf16.add_paragraph()
    p4.alignment = PP_ALIGN.CENTER
    p4.text = "Developed & Presented by:\nAjay M (Junior Software Developer)"
    p4.font.name = "Arial"
    p4.font.size = Pt(16)
    p4.font.bold = True
    p4.font.color.rgb = c_white
    p4.space_after = Pt(12)

    p5 = tf16.add_paragraph()
    p5.alignment = PP_ALIGN.CENTER
    p5.text = "Questions & Feedback Welcome 💬"
    p5.font.name = "Arial"
    p5.font.size = Pt(13)
    p5.font.bold = True
    p5.font.color.rgb = c_emerald

    # Save presentation
    output_path = os.path.join(DOC_DIR, "ServIQ_Project_Presentation.pptx")
    prs.save(output_path)
    print(f"Presentation successfully created at: {output_path}")

if __name__ == "__main__":
    create_presentation()
