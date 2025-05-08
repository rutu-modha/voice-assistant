const express = require('express')
const cors = require('cors')
const path = require('path')
const { spawn } = require("child_process")
const app = express()
app.use(cors())
app.use(express.json())
app.post("/", (req, res) => {
    const { text } = req.body;
    const cmdva = spawn("python", ["./voice_assistant.py", text])
    let op = ""
    cmdva.stdout.on("data", (data) => {
        op += data.toString()
    })
    cmdva.stderr.on("data", (data) => {
        console.log(data.toString())
    })
    cmdva.on("close", (code) => {
        res.json({ 
            message: op 
        })
    })
})
app.listen(5000, () => {
    console.log("Server is running at http://localhost:5000")
})