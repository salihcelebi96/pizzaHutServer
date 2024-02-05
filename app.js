const functions = require('firebase-functions');
const express = require('express');
const app = express();

// Express.js uygulamanızı burada konfigüre edin

// Yalnızca üstteki `app`'i kullanmaya devam edin, alttaki kısmı kaldırın.

exports.api = functions.https.onRequest(app);

// Daha fazla kod...




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



const PORT = 8000;



app.use(cors({
    origin: '*',
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
    credentials: true,
  }));

app.use('/icecekler', icecekler);
app.use('/pizza', pizza);
// app.use('/signup', signup);
app.use('/admin', admin);
app.use('/kampanyalar', kampanyalar);
app.use('/tatlilar', tatli);
app.use('/loginjwt', authRoutes);
app.use('/wings', wings);
app.use("/payment", payment);



app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
