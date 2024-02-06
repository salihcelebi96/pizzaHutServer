const functions = require('firebase-functions');
const express = require('express');
const app = express();



exports.myApi = functions.https.onRequest((request, response) => {
  response.json({ message: 'Merhaba, bu ücretsiz bir API!' });
});









const icecekler = require('./api/icecekler');
const pizza = require('./api/pizza');
// const signup = require('./signup');
const admin = require('./api/admin');
const kampanyalar = require('./api/kampanyalar');
const tatli = require('./api/tatli');
const wings = require('./api/wings');
const payment = require('./api/payment');
const authRoutes = require('./api/loginJwt');

const cors = require('cors');



const PORT = 8002;



app.use(cors({
    origin: '*',
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
    credentials: true,
  }));

app.use('/api/icecekler', icecekler);
app.use('/api/pizza', pizza);
// app.use('/signup', signup);
app.use('/api/admin', admin);
app.use('/api/kampanyalar', kampanyalar);
app.use('/api/tatlilar', tatli);
app.use('/api/loginjwt', authRoutes);
app.use('/api/wings', wings);
app.use("/api/payment", payment);



app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
exports.api = functions.https.onRequest(app);