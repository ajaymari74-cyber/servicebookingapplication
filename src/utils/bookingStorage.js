const DEFAULT_BOOKINGS = [
  {
    id: 10428,
    serviceId: 1,
    serviceName: "Professional Electrician",
    icon: "⚡",
    date: "2026-09-20",
    time: "10:00 AM",
    status: "Confirmed",
    customerName: "Alex Johnson",
    customerPhone: "+91 98765 43210",
    address: "Flat 402, Royal Palms, Sector 14",
    price: 499,
    bookingDate: "2026-09-15"
  },
  {
    id: 10394,
    serviceId: 3,
    serviceName: "AC Deep Cleaning & Service",
    icon: "❄️",
    date: "2026-09-22",
    time: "02:00 PM",
    status: "Confirmed",
    customerName: "Alex Johnson",
    customerPhone: "+91 98765 43210",
    address: "Flat 402, Royal Palms, Sector 14",
    price: 699,
    bookingDate: "2026-09-14"
  },
  {
    id: 10250,
    serviceId: 4,
    serviceName: "Full Home Deep Cleaning",
    icon: "🧹",
    date: "2026-08-30",
    time: "09:00 AM",
    status: "Completed",
    customerName: "Alex Johnson",
    customerPhone: "+91 98765 43210",
    address: "Flat 402, Royal Palms, Sector 14",
    price: 1899,
    bookingDate: "2026-08-28"
  }
];

export const getStoredBookings = () => {
  try {
    const raw = localStorage.getItem("serviqBookings");
    if (!raw) {
      localStorage.setItem("serviqBookings", JSON.stringify(DEFAULT_BOOKINGS));
      return DEFAULT_BOOKINGS;
    }
    return JSON.parse(raw);
  } catch (e) {
    console.error("Error reading bookings from localStorage:", e);
    return DEFAULT_BOOKINGS;
  }
};

export const saveBookings = (bookings) => {
  localStorage.setItem("serviqBookings", JSON.stringify(bookings));
};

export const addBooking = (bookingData) => {
  const current = getStoredBookings();
  const newBooking = {
    id: Math.floor(10000 + Math.random() * 90000),
    bookingDate: new Date().toISOString().split("T")[0],
    status: "Confirmed",
    ...bookingData
  };
  const updated = [newBooking, ...current];
  saveBookings(updated);
  return newBooking;
};

export const cancelBookingById = (id) => {
  const current = getStoredBookings();
  const updated = current.map(b => b.id === id ? { ...b, status: "Cancelled" } : b);
  saveBookings(updated);
  return updated;
};
