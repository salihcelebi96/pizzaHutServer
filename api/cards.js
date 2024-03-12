const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const router = express.Router();

dotenv.config();
mongoose.connect(process.env.MONGODB_URI);

const cardSchema = new mongoose.Schema({
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
  },
  activeUserEmail:{
    type: String,
    required: true,
  },
});

const Cards = mongoose.model('card', cardSchema);

router.get('/', async (req, res) => {
  try {
    const data = await Cards.find();
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

router.post('/', async (req, res) => {
  try {
    const {cardNumber, name, month, years , cvc, cardName,activeUserEmail  } = req.body;
    const newCard = new Cards({cardNumber, name, month, years, cvc, cardName,activeUserEmail });
    await newCard.save();
    res.status(201).json({ message: 'Card saved successfully!' });
  } catch (error) {
    console.error('Error during card save:', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

module.exports = router;
