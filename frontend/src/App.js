import React, { useState } from "react"
import "./App.css"
export default function App() {
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
            alert("Your speech is recognized successfully. Processing may take some time. Please wait a while while your assistant is performing the task given by you. It will respond to you after the task is completed.");
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
            speak(data.message)
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
    const speak = (text) => {
        utterance = new SpeechSynthesisUtterance(text)
        window.speechSynthesis.speak(text)
    }
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
