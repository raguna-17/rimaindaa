const API_BASE = "http://localhost:8000/api/";

// ===== Token Utilities =====
function getAccessToken() {
    return localStorage.getItem("access");
}

function setAccessToken(token) {
    localStorage.setItem("access", token);
}

function authHeaders() {
    const token = getAccessToken();
    return {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`,
    };
}

// ===== Auth =====
export async function login(username, password) {
    const res = await fetch(API_BASE + "token/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
    });
    if (!res.ok) throw new Error("login failed");
    const data = await res.json();
    setAccessToken(data.access);
    return data;
}

// ===== Memos =====
export async function getMemos() {
    const res = await fetch(API_BASE + "memos/", { headers: authHeaders() });
    if (!res.ok) throw new Error("failed to fetch memos");
    return res.json();
}

export async function createMemo(data) {
    const res = await fetch(API_BASE + "memos/", {
        method: "POST",
        headers: authHeaders(),
        body: JSON.stringify(data),
    });
    if (!res.ok) throw await res.json();
    return res.json();
}

// ===== Reminders =====
export async function createReminder(data) {
    const res = await fetch(API_BASE + "reminders/", {
        method: "POST",
        headers: authHeaders(),
        body: JSON.stringify(data),
    });
    if (!res.ok) throw await res.json();
    return res.json();
}

// ===== Notifications =====
export async function getNotifications() {
    const res = await fetch(API_BASE + "notifications/", { headers: authHeaders() });
    if (!res.ok) throw new Error("failed to fetch notifications");
    return res.json();
}

export async function markNotificationRead(id) {
    const res = await fetch(API_BASE + `notifications/${id}/`, {
        method: "PATCH",
        headers: authHeaders(),
        body: JSON.stringify({ is_read: true }),
    });
    if (!res.ok) throw new Error("failed to mark notification read");
    return res.json();
}
