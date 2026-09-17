/**
 * MockAPI Service for ServIQ User Management & Authentication
 * Supports:
 * - fullName (String)
 * - email (String)
 * - password (String)
 * - confirmPassword (String)
 * - phone (String)
 * - address (String)
 */

const DEFAULT_API_URL = import.meta.env.VITE_MOCK_API_URL || "https://6aab5d4cea0e22daa6dc21cb.mockapi.io/users";

export const getApiUrl = () => {
  return localStorage.getItem("serviq_mockapi_endpoint") || DEFAULT_API_URL;
};

export const setApiUrl = (url) => {
  if (!url) {
    localStorage.removeItem("serviq_mockapi_endpoint");
  } else {
    localStorage.setItem("serviq_mockapi_endpoint", url.trim());
  }
};

/**
 * Fetch all users from MockAPI (with local storage fallback)
 */
export const fetchUsers = async () => {
  const url = getApiUrl();
  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 4000);
    const response = await fetch(url, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
      signal: controller.signal
    });
    clearTimeout(timeoutId);

    if (response.ok) {
      const data = await response.json();
      if (Array.isArray(data)) {
        // Sync local cache
        localStorage.setItem("serviq_registered_users", JSON.stringify(data));
        return { success: true, users: data, source: "mockapi" };
      }
    }
  } catch (err) {
    console.warn("MockAPI fetch failed or timed out, using local storage cache:", err.message);
  }

  // Fallback to local storage
  try {
    const stored = localStorage.getItem("serviq_registered_users");
    const users = stored ? JSON.parse(stored) : [];
    return { success: true, users, source: "local" };
  } catch (e) {
    return { success: false, users: [], message: e.message };
  }
};

/**
 * Register a new user with the specified fields:
 * fullName, email, password, confirmPassword, phone, address
 */
export const registerUser = async ({
  fullName,
  email,
  password,
  confirmPassword,
  phone = "",
  address = ""
}) => {
  const cleanEmail = email.trim().toLowerCase();
  const cleanFullName = (fullName || "").trim();
  const cleanPhone = (phone || "").trim();
  const cleanAddress = (address || "").trim();

  // 1. Check existing users
  const { users } = await fetchUsers();
  const existing = users.find(u => (u.email || "").toLowerCase() === cleanEmail);
  if (existing) {
    return {
      success: false,
      message: "An account with this email already exists."
    };
  }

  const payload = {
    fullName: cleanFullName,
    name: cleanFullName, // for backwards compatibility
    email: cleanEmail,
    password,
    confirmPassword,
    phone: cleanPhone,
    address: cleanAddress,
    createdAt: new Date().toISOString()
  };

  const url = getApiUrl();
  let createdUser = null;
  let savedSource = "local";

  // 2. Try POST to MockAPI
  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 5000);
    const response = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
      signal: controller.signal
    });
    clearTimeout(timeoutId);

    if (response.ok) {
      createdUser = await response.json();
      savedSource = "mockapi";
    } else {
      console.warn(`MockAPI POST responded with status ${response.status}. Using local storage.`);
    }
  } catch (err) {
    console.warn("MockAPI POST request error:", err.message);
  }

  // 3. Resilient fallback to local storage
  if (!createdUser) {
    createdUser = {
      id: Date.now().toString(),
      ...payload
    };
  }

  // Update local storage registered accounts list
  try {
    const stored = localStorage.getItem("serviq_registered_users");
    const currentList = stored ? JSON.parse(stored) : [];
    const updatedList = [...currentList.filter(u => (u.email || "").toLowerCase() !== cleanEmail), createdUser];
    localStorage.setItem("serviq_registered_users", JSON.stringify(updatedList));
    localStorage.setItem("serviqUser", JSON.stringify(createdUser));
  } catch (err) {
    console.error("Failed to update local storage", err);
  }

  return {
    success: true,
    user: createdUser,
    source: savedSource
  };
};

/**
 * Login user by querying MockAPI or checking local storage cache & demo credentials
 */
export const loginUser = async (email, password) => {
  const cleanEmail = email.trim().toLowerCase();

  // 1. Check demo credentials
  if (cleanEmail === "demo@serviq.com" || cleanEmail === "user@serviq.com") {
    const demoUser = {
      id: "demo-user-1",
      fullName: "Alex Johnson",
      name: "Alex Johnson",
      email: cleanEmail,
      phone: "+91 98765 43210",
      address: "42 Greenfield Boulevard, Sector 12"
    };
    return { success: true, user: demoUser, isDemo: true };
  }

  // 2. Try to query MockAPI by email
  const url = getApiUrl();
  try {
    const queryUrl = `${url}?email=${encodeURIComponent(cleanEmail)}`;
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 4000);
    const response = await fetch(queryUrl, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
      signal: controller.signal
    });
    clearTimeout(timeoutId);

    if (response.ok) {
      const results = await response.json();
      if (Array.isArray(results) && results.length > 0) {
        const found = results.find(u => (u.email || "").toLowerCase() === cleanEmail && u.password === password);
        if (found) {
          return { success: true, user: found, source: "mockapi" };
        } else {
          return { success: false, message: "Invalid email or password." };
        }
      }
    }
  } catch (err) {
    console.warn("MockAPI login query error, falling back to cached users:", err.message);
  }

  // 3. Check cached / local registered users
  try {
    const stored = localStorage.getItem("serviq_registered_users");
    if (stored) {
      const users = JSON.parse(stored);
      const found = users.find(u => (u.email || "").toLowerCase() === cleanEmail && u.password === password);
      if (found) {
        return { success: true, user: found, source: "local" };
      }
    }
  } catch (err) {
    console.error("Local user lookup failed", err);
  }

  return {
    success: false,
    message: "Invalid email or password. You can also use the Demo Account or Register."
  };
};
