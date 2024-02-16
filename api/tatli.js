const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const dotenv = require('dotenv');

const app = express();
const router = express.Router();


app.use(express.json());
app.use(cors());
app.use(express.urlencoded({ extended: true }));



dotenv.config();
// MongoDB bağlantısı
mongoose.connect(process.env.MONGODB_URI);

// MongoDB şeması ve modeli
const tatliSchema = new mongoose.Schema({
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
const Tatlilar = mongoose.model('tatli', tatliSchema);



router.get('/', async (req, res) => {
  try {
    const data = await Tatlilar.find();
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
    
  }
});


router.post('/', async (req, res) => {
  try {
    const { tür, fiyat, url } = req.body;
    const newTatlı = new Tatlilar({
      tür,
      fiyat,
      url,
    });
    const savedTatlı = await newTatlı.save(); // MongoDB'ye kaydedin
    tatlilar.push(savedTatlı); // Yerel dizinize de ekleyin
    res.status(201).json(savedTatlı);
  } catch (error) {
    console.error('Post işlemi sırasında bir hata oluştu:', error);
    res.status(500).json({ error: 'Internal Server Error' });
    console.log(req.body);
  }
});




module.exports = router;