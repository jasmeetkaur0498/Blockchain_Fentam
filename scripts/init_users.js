// scripts/init_users.js
const { MongoClient } = require("mongodb");
const { ethers } = require("hardhat");

const uri = "mongodb://localhost:27017"; // update if needed
const client = new MongoClient(uri);

const users = [
  {
    name: "Admin",
    email: "admin@fentam.com",
    role: "admin",
    walletAddress: "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
    approved: true
  },
  {
    name: "Manufacturer A",
    email: "manufacturer@fentam.com",
    role: "manufacturer",
    walletAddress: "0x70997970C51812dc3A010C7d01b50e0d17dc79C8",
    approved: true
  },
  {
    name: "Distributor B",
    email: "distributor@fentam.com",
    role: "distributor",
    walletAddress: "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC",
    approved: true
  },
  {
    name: "Retailer C",
    email: "retailer@fentam.com",
    role: "retailer",
    walletAddress: "0x90F79bf6EB2c4f870365E785982E1f101E93b906",
    approved: true
  },
  {
    name: "Pharmacy D",
    email: "pharmacy@fentam.com",
    role: "pharmacy",
    walletAddress: "0x15d34AAf54267DB7D7c367839AAf71A00a2C6A65",
    approved: true
  }
];


async function main() {
  const accounts = await ethers.getSigners();

  await client.connect();
  const db = client.db("fentam");
  const collection = db.collection("users");

  await collection.deleteMany({}); // Clear old data

  const userDocs = users.map((user, idx) => ({
    ...user,
    email: `${user.role}@fentam.com`,
    walletAddress: accounts[idx].address,
    approved: user.role === "admin", // Only admin is auto-approved
  }));

  await collection.insertMany(userDocs);
  console.log("✅ Users initialized in MongoDB");

  await client.close();
}

main().catch(console.error);
