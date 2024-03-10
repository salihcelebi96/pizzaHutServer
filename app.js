const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const cors = require('cors');

// CORS middleware
app.use(cors());

// Body-parser middleware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// Routers
const icecekler = require('./api/icecekler');
const pizza = require('./api/pizza');
const admin = require('./api/admin');
const kampanyalar = require('./api/kampanyalar');
const tatli = require('./api/tatli');
const wings = require('./api/wings');
const payment = require('./api/payment');
const authRoutes = require('./api/loginJwt');
const address = require('./api/address');



const PORT = 8004;

app.use('/api/pizza', pizza);
app.use('/api/icecekler', icecekler);
app.use('/api/admin', admin);
app.use('/api/kampanyalar', kampanyalar);
app.use('/api/tatlilar', tatli);
app.use('/api/loginjwt', authRoutes);
app.use('/api/wings', wings);
app.use("/api/payment", payment);
app.use("/api/address", address);


// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
