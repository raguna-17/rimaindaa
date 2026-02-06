import { useEffect, useState } from "react";
import client from "../api/client";

type Note = {
    id: number;
    title: string;
};

export default function Memos() {
    const [memos, setMemos] = useState<Note[]>([]);

    useEffect(() => {
        const token = localStorage.getItem("token");
        if (token) client.defaults.headers.common["Authorization"] = `Bearer ${token}`;

        client.get("/memos/").then(res => setMemos(res.data));
    }, []);

    return (
        <div>
            <h1>メモ一覧</h1>
            <ul>
                {memos.map(m => (
                    <li key={m.id}>{m.title}</li>
                ))}
            </ul>
        </div>
    );
}
