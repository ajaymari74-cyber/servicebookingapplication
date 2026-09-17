# ServIQ – On-Demand Doorstep Home & Electrical Services Booking Platform

**Project Technical Documentation**  
**Author:** Ajay M (Junior Software Developer)  
**Document Version:** 1.0 (Production Release)  
**Date:** September 2026  
**Technology Stack:** React.js (v19), Vite (v6), JavaScript (ES6+), CSS3, React Router v6, LocalStorage API  

---

## Author & Project Metadata

| Field | Details |
| :--- | :--- |
| **Project Title** | **ServIQ – Doorstep Home & Electrical Services Booking Web Application** |
| **Prepared By** | **Ajay M** |
| **Designation / Role** | **Junior Software Developer** |
| **Frontend Framework** | React.js (v19) with Vite (v6) |
| **Application Type** | Single Page Application (SPA) with Client-Side Routing |
| **Styling Architecture**| Custom Modern CSS Design System (Flexbox, Grid, Glassmorphism) |
| **State & Persistence** | React Hooks (`useState`, `useEffect`, `useMemo`), Context API, LocalStorage |
| **Word Document File** | [`ServIQ_Project_Documentation.docx`](file:///d:/Fontend%20Projects/serviq/ServIQ_Project_Documentation.docx) |

---

## 1. Introduction

**ServIQ** is an on-demand doorstep home and electrical services web application built with React.js and modern frontend tooling. In urban communities, finding verified, certified, and punctual technicians for routine domestic repairs—such as electricians, master plumbers, air conditioning technicians, home cleaners, carpenters, and appliance mechanics—often entails uncertain pricing and poor service visibility. ServIQ eliminates this friction by providing a transparent, intuitive digital booking platform.

### Core Capabilities:
- **Service Catalog Discovery:** Instant browsing across 8 specialized domestic repair domains.
- **Dynamic Category Filtering:** Real-time filtering by category (Electrical, Plumbing, Cleaning, AC & Appliances, Pest Control, Painting, Carpentry).
- **Instant Keyword Search:** Real-time search by service name, description, and domain keywords.
- **Multi-Criteria Sorting:** Sort by popularity/recommended, customer ratings, and price (low-to-high, high-to-low).
- **Rich Media & Photo Galleries:** High-definition photography for every service, featuring interactive multi-view photo galleries (e.g., for Pest Control & Sanitization).
- **Comprehensive Service Inclusions:** Clear display of what is covered, warranty guarantees (30-day rework warranty), duration, and fixed transparent pricing.
- **3-Step Frictionless Scheduling:** Fast appointment date selection, time-slot picker (6 daily slots), customer address input, and flexible payment options ("Pay after Service" or "Pay Online").
- **Official Booking Receipt:** Automatic generation of an official receipt with a unique reference ID (e.g., `#SRV-15376`) and verified technician assignment.
- **Persistent Booking Management ("My Bookings"):** Real-time booking dashboard with status tab filtering (All, Confirmed, Completed, Cancelled) and modal-confirmed appointment cancellations.

---

## 2. Objectives

1. **Responsive & Modern UI Architecture:** Build a responsive, fast web interface tailored for homeowners across desktop, tablet, and mobile devices.
2. **Component-Based Modularity:** Implement clean, decoupled, and reusable React components (`ServiceCard`, `ServiceList`, `BookingForm`, `NavBar`, `Footer`, `Button`).
3. **Centralized Client-Side State Management:** Implement React state handling via React Hooks (`useState`, `useEffect`, `useMemo`) and React Context (`AuthContext`).
4. **Persistent Local Storage Architecture:** Provide a persistent client-side data layer using browser LocalStorage for appointment schedules, user authentication, and pre-seeded records.
5. **Dynamic Client-Side Routing:** Enable seamless multi-page transitions and deep-linking using React Router v6 without full-page reloads.
6. **Rich Media Asset Integration:** Incorporate authentic photography across all UI views (card banners, hero banners, order summaries, receipts, and booking dashboards).
7. **Transparent User-Centric Flow:** Guarantee upfront fixed pricing with zero hidden diagnostic fees and convenient "Pay After Service" terms.

---

## 3. Technologies Used

| Technology | Category | Purpose in ServIQ |
| :--- | :--- | :--- |
| **React.js (v19)** | UI Library | Component-based declarative user interface construction and virtual DOM rendering. |
| **Vite (v6)** | Build Tool & Dev Server | Ultra-fast Hot Module Replacement (HMR) and optimized ES module bundling. |
| **JavaScript (ES6+)** | Core Language | Application logic, state manipulation, array filtering, and asynchronous actions. |
| **HTML5** | Markup | Semantic layout architecture, accessible form controls, and structured content. |
| **CSS3** | Styling & Design System | Custom color variables, responsive flexbox & grid layouts, glassmorphism, and micro-interactions. |
| **React Router (v6)** | Client Routing | Declarative browser history routing, parameterized URL matching, and smooth page switches. |
| **React Context API** | State Management | Global authentication state propagation across all component hierarchies. |
| **LocalStorage API** | Data Persistence | Synchronous local client-side persistence for booking records and user profiles. |
| **VS Code** | Development IDE | Source code authoring, linting, debugging, and extensions integration. |
| **Git / GitHub** | Version Control | Distributed version control and source code repository management. |

---

## 4. System Requirements

### 4.1 Hardware Requirements
- **Processor:** Intel Core i3 / AMD Ryzen 3 or higher (dual-core 2.0 GHz minimum).
- **RAM:** 4 GB minimum (8 GB or higher recommended).
- **Storage Space:** 10 GB of available hard disk / SSD space.
- **Display Resolution:** 1366 x 768 minimum resolution (Full HD 1920 x 1080 recommended).

### 4.2 Software Requirements
- **Operating System:** Windows 10 / Windows 11, macOS, or Linux.
- **Node.js Runtime:** Node.js version 18.x or 20.x LTS.
- **Package Manager:** npm (version 9.x+) / yarn / pnpm.
- **Code Editor:** Visual Studio Code.
- **Web Browser:** Google Chrome 110+, Microsoft Edge 110+, Mozilla Firefox 110+, or Apple Safari 16+.

---

## 5. Project Structure

```
serviq/
├── index.html                       # HTML5 Root Entry Point & SEO Metadata
├── package.json                     # Project Manifest & NPM Dependencies
├── vite.config.js                   # Vite Bundler & Build Configuration
│
├── public/                          # Static Web Assets
│   └── vite.svg
│
├── documentation_screenshots/       # High-Resolution UI Module Captures
│   ├── 01_home_page.png
│   ├── 02_all_services_catalog.png
│   ├── 03_service_details_electrician.png
│   ├── 04_service_details_pest_control_gallery.png
│   ├── 05_schedule_appointment_booking.png
│   ├── 06_booking_confirmed_receipt.png
│   └── 07_my_bookings_dashboard.png
│
├── ServIQ_Project_Documentation.docx # Complete Microsoft Word Technical Document
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
        └── bookingStorage.js        # LocalStorage CRUD Functions for Bookings
```

---

## 6. Application Modules

### 6.1 Home & Hero Module (`Home.jsx`)
Acts as the user gateway featuring a bold value proposition, search bar, quick category pills, popular services grid with authentic photography, a 3-step "How It Works" section, trust badges, and a call-to-action banner.

### 6.2 Service Catalog & Filtering Module (`Services.jsx` & `ServiceList.jsx`)
Presents all 8 services in a responsive grid. Offers instant category filtering pills (All, Electrical, Plumbing, AC & Appliances, Cleaning, Pest Control, Painting, Carpentry), keyword search, and multi-option sorting (Recommended, Highest Rated, Price Low-High, Price High-Low).

### 6.3 Service Details & Interactive Gallery Module (`ServiceDetails.jsx`)
Full-page inspection for any service. Features a full-width hero image banner (340px height), an interactive thumbnail photo gallery switcher (e.g. for Pest Control & Sanitization), complete description, inclusions checklist, service guarantees, and a sticky booking sidebar.

### 6.4 Appointment Scheduling & Booking Module (`Booking.jsx` & `BookingForm.jsx`)
Features a top "Service Spotlight" banner and a 3-step booking form:
1. **Date & Time:** Date picker (prevents past dates) and 6 standard time slots.
2. **Customer Details & Address:** Name, phone, street address, and optional landmark (auto-filled if logged in).
3. **Payment Preference:** Choice between "💵 Pay after Service" and "💳 Pay Online".

### 6.5 Booking Confirmation & Official Receipt Module (`BookingSuccess.jsx`)
Displays a verified confirmation receipt upon booking creation, generating a unique booking ID (e.g., `#SRV-15376`), service thumbnail, appointment time, and direct navigation links.

### 6.6 "My Bookings" Management Dashboard Module (`MyBookings.jsx`)
Enables users to manage appointments with tabbed filters (All, Confirmed, Completed, Cancelled). Confirmed appointments can be cancelled with an instant modal dialog, updating LocalStorage state in real time.

### 6.7 User Authentication & Profile Session Module (`AuthContext.jsx` & `Login.jsx`)
Provides global session handling via React Context. Automatically pre-fills customer booking details when signed in.

---

## 7. Functional Requirements

- **FR-1 (Browsing):** Display full catalog of 8 services with photography, pricing, and ratings.
- **FR-2 (Filtering):** Instant filtering across 8 domestic categories.
- **FR-3 (Search):** Dynamic keyword matching across titles, descriptions, and domains.
- **FR-4 (Sorting):** Dynamic sorting by rating, price low-to-high, price high-to-low, or recommendation.
- **FR-5 (Details):** Full breakdown of inclusions, warranties, duration, and price.
- **FR-6 (Gallery):** Multi-photo gallery thumbnail switching for supported services.
- **FR-7 (Slot Picking):** Validation against past dates; selection of 6 daily time slots.
- **FR-8 (Address Capture):** Mandatory validation for name, phone, and street address.
- **FR-9 (Payment Choice):** Selection between cash-after-service and online checkout.
- **FR-10 (Receipt Creation):** Automatic numeric booking ID generation and itemized receipt display.
- **FR-11 (Persistence):** LocalStorage storage of all scheduled appointments.
- **FR-12 (Cancellation):** Two-step confirmation modal for cancelling active appointments.

---

## 8. React Concepts Used

### 8.1 Functional Components & Props
```jsx
// src/Components/ServiceCard.jsx
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
};
```

### 8.2 Interactive State (`useState`)
```jsx
const [activeImage, setActiveImage] = React.useState(service?.image || null);
const [selectedCategory, setSelectedCategory] = useState("All");
const [searchQuery, setSearchQuery] = useState("");
const [sortBy, setSortBy] = useState("popular");
```

### 8.3 Performance Optimization (`useMemo`)
```jsx
const filteredServices = useMemo(() => {
  let result = servicesData.filter((service) => {
    const matchesCategory = selectedCategory === "All" || 
      service.category.toLowerCase() === selectedCategory.toLowerCase();
    const matchesSearch = service.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          service.description.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCategory && matchesSearch;
  });
  if (sortBy === "price-low") result.sort((a, b) => a.price - b.price);
  else if (sortBy === "price-high") result.sort((a, b) => b.price - a.price);
  else if (sortBy === "rating") result.sort((a, b) => b.rating - a.rating);
  return result;
}, [selectedCategory, searchQuery, sortBy]);
```

### 8.4 Global Session Management (`useContext`)
```jsx
const { currentUser } = useAuth();
useEffect(() => {
  if (currentUser) {
    setCustomerName(currentUser.fullName || "");
    setCustomerPhone(currentUser.phone || "");
    setAddress(currentUser.address || "");
  }
}, [currentUser]);
```

---

## 9. Routing Architecture

| URL Path | Target Component | Parameters / Query | Purpose |
| :--- | :--- | :--- | :--- |
| `/` | `Home` | None | Landing page with hero, search, category pills & popular services. |
| `/services` | `Services` | `?cat=Category&q=Search` | Full service catalog with filters, search, and sorting. |
| `/services/:id` | `ServiceDetails` | `id: Service ID` | Detailed service view with full-bleed hero banner & photo gallery. |
| `/book/:id?` | `Booking` | `id: Service ID (Optional)` | Appointment scheduling screen with spotlight and 3-step form. |
| `/booking-success` | `BookingSuccess` | `?id=Booking ID` | Official booking confirmed receipt with booking reference `#SRV-XXXX`. |
| `/my-bookings` | `MyBookings` | None | Customer appointment dashboard with status tabs and cancellation modal. |
| `/login` | `Login` | None | User authentication login form with demo credential support. |
| `/register` | `Register` | None | New user onboarding and customer account creation. |

---

## 10. Data Architecture & Schema

### Service Schema (`src/data/servicesData.js`)
```javascript
{
  id: 1,
  name: "Professional Electrician",
  category: "Electrical",
  icon: "⚡",
  image: electricianImg,          // Photographic asset
  gallery: [pestImg, pestImg2],   // Multi-image gallery array
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
}
```

### Booking Schema (`src/utils/bookingStorage.js`)
```javascript
{
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
}
```

---

## 11. Application Flow

```
                [ Customer / User ]
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
                              Cancellation Modal)
```

---

## 12. Important Modules Screenshots & UI Walkthrough

All screenshots were captured live from the running ServIQ web application and are embedded in the Word Document (`ServIQ_Project_Documentation.docx`):

1. **Home Page (`01_home_page.png`):** Hero headline, search bar, category pills, and popular service cards with real photos.
2. **All Services Catalog (`02_all_services_catalog.png`):** Category pills, search bar, sort dropdown, and full 8-service responsive grid.
3. **Service Details - Electrician (`03_service_details_electrician.png`):** 340px featured hero image banner, inclusions checklist, guarantees, and sticky fixed-price booking box.
4. **Service Details - Pest Control Gallery (`04_service_details_pest_control_gallery.png`):** Interactive photo gallery switcher with multiple image angles.
5. **Schedule Appointment Page (`05_schedule_appointment_booking.png`):** Service spotlight card, date picker, 6 time slots, customer contact, and payment radio buttons.
6. **Official Booking Confirmed Receipt (`06_booking_confirmed_receipt.png`):** Unique booking ID `#SRV-15376` for Ajay M, service photo thumbnail, appointment timing, and address.
7. **My Bookings Dashboard (`07_my_bookings_dashboard.png`):** Scheduled appointments with real thumbnails, status badges (`Confirmed`), and interactive cancellation modal.

---

## 13. Testing & Verification

| Test Case | Module Tested | Input Data | Expected Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Home Page | Open `http://localhost:5173` | Hero, search bar, and 6 service cards with real images render cleanly. | **PASS** |
| **TC-02** | Category Filter | Click 'Cleaning' pill | Only 'Full Home Deep Cleaning' card is displayed in the grid. | **PASS** |
| **TC-03** | Search Engine | Type 'plumb' into search | Master Plumber Service card displayed; non-matching services hidden. | **PASS** |
| **TC-04** | Service Details | Click 'Details' on Electrician | Hero image banner loads, inclusions and guarantees display, sticky sidebar active. | **PASS** |
| **TC-05** | Interactive Gallery | Click thumb 2 on Pest Control | Active hero banner switches smoothly to second sanitization image. | **PASS** |
| **TC-06** | Slot Selection | Click '01:00 PM' slot button | Selected slot highlights with blue border and updates order summary. | **PASS** |
| **TC-07** | Form Validation | Submit empty booking form | Displays inline error: 'Please fill in your name, phone, and address.' | **PASS** |
| **TC-08** | Booking Creation | Name: Ajay M, Phone: 9876543210 | Saved into LocalStorage, redirects to `/booking-success` with ID `#SRV-15376`. | **PASS** |
| **TC-09** | Receipt Display | Open `/booking-success?id=15376`| Receipt card displays verified badge, service photo, customer name, date & time. | **PASS** |
| **TC-10** | Appointment Cancel | Click 'Cancel' in My Bookings | Modal prompts confirmation; on confirm, status updates to 'Cancelled'. | **PASS** |

---

## 14. Advantages & Key Highlights

- **Ultra-Clean & Intuitive UI/UX:** Clutter-free design allowing users to book within 60 seconds.
- **Upfront Fixed Pricing:** Transparent rates eliminate anxiety over hidden diagnostic charges.
- **Zero-Friction Scheduling:** Customers book without mandatory upfront payments via "Pay after Service".
- **Authentic Visuals:** Real service photography fosters customer trust and clear expectations.
- **Decoupled Architecture:** Clean component separation ensures maintainability and code longevity.
- **High Performance:** Instant filtering and transitions powered by Vite and `useMemo`.

---

## 15. Future Enhancements

- **Payment Gateway Integration:** Razorpay and Stripe checkout for cards, net banking, and UPI.
- **SMS & WhatsApp Alerts:** Automated dispatch notifications via Twilio.
- **Live GPS Tracking:** Real-time map tracking of technician arrival.
- **Technician & Admin Portal:** Job acceptance and status updates for field technicians.
- **Reviews & Ratings:** Customer review submissions with photos and star ratings.

---

## 16. Conclusion

The **ServIQ On-Demand Doorstep Home & Electrical Services Booking Platform** demonstrates the power of React.js and modern frontend tooling in delivering a robust, production-ready, and user-centric web solution. By combining modular component architecture, centralized state handling, persistent local storage, and authentic high-resolution photography, ServIQ provides a seamless, reliable, and visually engaging booking experience.

The project highlights complete proficiency in component lifecycle management, hook optimization, declarative routing, and data persistence, establishing a solid foundation for commercial scalability.
