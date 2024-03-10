const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const router = express.Router();




dotenv.config();
mongoose.connect(process.env.MONGODB_URI);

const paymentSchema = new mongoose.Schema({

  cardNumber: {
    type: String,
    required: true,
  },
  name: {
    type: String,
    required: true,
  },
  month: {
    type: String,
    required: true,
  },
  years:{
    type: String,
    required: true,
  },
  cvc: {
    type: String,
    required: true,
  },
  cardName:{
    type: String,
    required: true,
  }
});

const Payments = mongoose.model('payment', paymentSchema);

router.get('/', async (req, res) => {
  try {
    const data = await Payments.find();
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

router.post('/', async (req, res) => {
  try {
    const {cardNumber, name, month, years , cvc, cardName  } = req.body;
    const newPayment = new Payments({cardNumber, name, month, years, cvc, cardName });
    await newPayment.save();
    res.status(201).json({ message: 'Payment saved successfully!' });
  } catch (error) {
    console.error('Error during payment:', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});




module.exports = router;