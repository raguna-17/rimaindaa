import { createMemo, createReminder, getNotifications, markNotificationRead } from './api.js';

document.addEventListener("DOMContentLoaded", () => {
    const reminderForm = document.getElementById("reminder-form");
    const memoTitleInput = document.getElementById("memo-title");
    const remindAtInput = document.getElementById("remind-at");
    const notificationList = document.getElementById("notification-list");
    const error = document.getElementById("error");
    const logoutBtn = document.getElementById("logout-btn");
    logoutBtn.addEventListener("click", () => {
        // ローカルストレージのトークン削除
        localStorage.removeItem("access");

        // ログインページにリダイレクト
        window.location.href = "/login/";
    });
    // -------------------------
    // Reminder 作成フォーム
    // -------------------------
    reminderForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        error.textContent = "";

        const title = memoTitleInput.value.trim();
        const remindAt = remindAtInput.value;

        if (!title) {
            error.textContent = "メモタイトルを入力してください";
            return;
        }
        if (!remindAt) {
            error.textContent = "日時を入力してください";
            return;
        }

        try {
            // まずメモを作成
            const memo = await createMemo({ title });

            // 作成したメモにリマインダーをセット
            await createReminder({ note: memo.id, remind_at: remindAt });

            // フォームリセット
            reminderForm.reset();

            // 通知ロード
            await loadNotifications();
        } catch (err) {
            console.error(err);
            error.textContent = "作成失敗";
        }
    });

    // -------------------------
    // Notifications ロード
    // -------------------------
    async function loadNotifications() {
        notificationList.innerHTML = "";
        try {
            const notifications = await getNotifications();
            notifications.forEach(notif => {
                const li = document.createElement("li");
                li.textContent = notif.message + (notif.is_read ? " ✅" : " 🔔");

                li.onclick = async () => {
                    if (!notif.is_read) {
                        await markNotificationRead(notif.id);
                        await loadNotifications();
                    }
                };

                notificationList.appendChild(li);
            });
        } catch (err) {
            console.error(err);
            error.textContent = "通知取得失敗";
        }
    }

    // 初期ロード
    loadNotifications();
});
