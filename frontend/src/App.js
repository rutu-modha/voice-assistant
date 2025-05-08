import React, { useState } from "react"
import "./App.css"
export default function App() {
    // eslint-disable-next-line
    const [res, setRes] = useState("")
    // eslint-disable-next-line
    const [listen, setListen] = useState(false)
    const [value, setValue] = useState("")
    const startListening = () => {
        const recognition = new window.webkitSpeechRecognition();
        recognition.lang = 'en-US';
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;
        recognition.onstart = () => {
            setListen(true)
        };
        recognition.onresult = async (event) => {
            const transcript = event.results[0][0].transcript;
            setListen(false)
            alert(`You said: ${transcript}`);
            const res = await fetch("http://localhost:5000/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    text: transcript
                })
            });
            const data = await res.json();
            setValue(prev => prev + "\nYou: " + transcript + "\nBot: " + data.message + "\n")
        };
        recognition.onerror = (event) => {
            console.error('Error occurred in recognition: ' + event.error);
            setListen(false)
        };
        recognition.start();
        recognition.onend = () => {
            setListen(false)
        };
    };
    return (
        <div>
            <h1>Voice Assistant</h1>
            <p>Welcome to your voice assistant application!</p>
            <p>Click the button below to start listening.</p>
            <button onClick={startListening}>Start Listening</button>
            <div>
                <pre>{value}</pre>
            </div>
        </div>
    )
}