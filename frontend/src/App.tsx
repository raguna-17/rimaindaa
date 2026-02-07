import { useState } from "react";
import axios from "axios";

type Note = { id: number; title: string };
type Reminder = { id: number; note: Note; remind_at: string };

const API_BASE = "https://rimaindaa.onrender.com/api";



function App() {
  // ログイン
  const [token, setToken] = useState<string | null>(localStorage.getItem("token"));
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  // リマインダー
  const [noteTitle, setNoteTitle] = useState("");
  const [remindAt, setRemindAt] = useState("");
  const [reminders, setReminders] = useState<Reminder[]>([]);

  // JWTセット
  const setAuthHeader = (accessToken: string) => {
    axios.defaults.headers.common["Authorization"] = `Bearer ${accessToken}`;
  };

  // ログイン
  const login = async () => {
    try {
      const response = await axios.post(`${API_BASE}/token/`, {
        username,
        password,
      });
      const access = response.data.access;
      setToken(access);
      localStorage.setItem("token", access);
      setAuthHeader(access);
      fetchReminders(access);
    } catch (err: any) {
      alert("ログイン失敗");
      console.log(err.response?.data);
    }
  };

  // ログアウト
  const logout = () => {
    setToken(null);
    localStorage.removeItem("token");
    axios.defaults.headers.common["Authorization"] = "";
  };

  // リマインダー取得
  // リマインダー取得関数（元の形）
  const fetchReminders = async (currentToken?: string) => {
    const t = currentToken || token; // 引数があればそれを使う
    if (!t) return;

    setAuthHeader(t);

    try {
      const res = await axios.get<Reminder[]>(`${API_BASE}/reminders/`);
      setReminders(res.data);
    } catch (err: any) {
      console.log(err.response?.data); // バリデーションエラーや通信エラーを確認
    }
  };

  

  // リマインダー追加
  const addReminder = async () => {
    if (!noteTitle || !remindAt) return alert("タイトルと日時を入力");

    try {
      if (!token) return alert("Not logged in");
      setAuthHeader(token); 
      // Note作成
      const noteRes = await axios.post(`${API_BASE}/memos/`, { title: noteTitle });
      const noteId = noteRes.data.id;

      // Reminder作成
      const reminderRes = await axios.post(`${API_BASE}/reminders/`, {
        note_id: noteId,
        remind_at: new Date(remindAt).toISOString(),
      });

      setReminders((prev) => [...prev, reminderRes.data]);
      setNoteTitle("");
      setRemindAt("");
    } catch (err: any) {
      console.log(err.response?.data);
      alert("リマインダー追加失敗");
    }
  };

  // リマインダー削除
  const deleteReminder = async (id: number) => {
    try {
      await axios.delete(`${API_BASE}/reminders/${id}/`);
      setReminders((prev) => prev.filter((r) => r.id !== id));
    } catch (err: any) {
      console.log(err.response?.data);
      alert("削除失敗");
    }
  };

  // ログイン前
  if (!token) {
    return (
      <div>
        <h1>Login</h1>
        <input
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button onClick={login}>Login</button>
      </div>
    );
  }

  // ログイン後ホーム画面
  return (
    <div>
      <h1>Home</h1>
      <button onClick={logout}>Logout</button>

      <h2>Add Reminder</h2>
      <input
        placeholder="Note title"
        value={noteTitle}
        onChange={(e) => setNoteTitle(e.target.value)}
      />
      <input
        type="datetime-local"
        value={remindAt}
        onChange={(e) => setRemindAt(e.target.value)}
      />
      <button onClick={addReminder}>Add Reminder</button>

      <h2>Reminders</h2>
      <ul>
        {reminders.map((r) => (
          <li key={r.id}>
            {r.note.title} at {new Date(r.remind_at).toLocaleString()}
            <button onClick={() => deleteReminder(r.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
