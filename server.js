// server.js
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { initializeApp, applicationDefault, cert } = require('firebase-admin/app');
const { getFirestore } = require('firebase-admin/firestore');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Initialize Firebase Admin SDK (if you need it, otherwise you can skip this)
initializeApp({
    credential: applicationDefault(),
});

// Route to handle air quality request
app.post('/api/air-quality', (req, res) => {
    const { latitude, longitude } = req.body;

    // Here you would normally interact with GEE to fetch data
    // For demonstration, we will return a mock response
    const mockResponse = {
        location: { latitude, longitude },
        airQuality: 'Moderate',
        suggestions: [
            'Consider reducing vehicle usage.',
            'Plant more trees in the area.',
            'Encourage the use of public transportation.',
        ],
    };

    res.json(mockResponse);
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});