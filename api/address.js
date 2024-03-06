const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');
const dotenv = require('dotenv');

dotenv.config();

mongoose.connect(process.env.MONGODB_URI);

const addressSchema = new mongoose.Schema({
    addressName: {
        type: String,
        required: true,
    },
    neighbourHood: {
        type: String,
        required: true,
    },
    addressDetail: {
        type: String,
        required: true,
    },
    district: {
        type: String,
        required: true,
    },
    city: {
        type: String,
        required: true,
    },
    user:{
        type: String,
        required: true,
    }
});

const Address = mongoose.model("Address", addressSchema);

router.get("/", async (req, res) => {
    try {
        const data = await Address.find();
        res.json(data);
    } catch (error) {
        res.status(500).json({ error: "Internal Server Error" });
    }
});

router.post("/", async (req, res) => {
    const { addressName, neighbourHood, addressDetail, district, city, user } = req.body;
    try {
        const savedAddress = await Address.create({
           city, 
           district,
           neighbourHood,
           addressDetail,
           addressName,
           user
            
          });   
            
            res.status(201).json(savedAddress);
    } catch (error) {
        res.status(500).json({ error: "Internal Server Error" });
    }
});        
       


module.exports = router;
