const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const dotenv = require('dotenv');
const router = express.Router();
const app = express();

dotenv.config();

app.use(cors({
  origin: '*',
  methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
  credentials: true,
}));






app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', '*');
  res.header('Access-Control-Allow-Methods', '*');
  next();
});

mongoose.connect(process.env.MONGODB_URI);

const icecekSchema = new mongoose.Schema({
  tür: {
    type: String,
    required: true,
  },
  fiyat: {
    type: Number,
    required: true,
  },
  url: {
    type: String,
    required: true,
  },
});

const Icecekler = mongoose.model('icecek', icecekSchema);

app.use(express.json());

router.get('/', async (req, res) => {
  try {
    const data = await Icecekler.find();
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

router.post('/', async (req, res) => {
  const { tür, fiyat, url } = req.body;

  try {
    const savedIcecek = await Icecekler.create({
      tür,
      fiyat,
      url,
    });

    res.status(201).json(savedIcecek);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});






module.exports = router;