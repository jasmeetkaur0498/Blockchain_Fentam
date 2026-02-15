# 🔗 Fentanyl Supply Chain Management (FENTAM)

**A blockchain-based supply chain management system for tracking fentanyl and controlled substances from manufacturer to end consumer.**

This project ensures transparency, accountability, and prevents product misplacement through decentralized verification and role-based approval workflows.

**Status**: ✅ Production Ready | **Version**: 1.0.0 | **Date**: February 2026

---

## 📋 Table of Contents
- [🚀 Quick Start (5 Minutes)](#quick-start)
- [🎯 Project Overview](#project-overview)
- [🏗️ System Architecture](#system-architecture)
- [📊 Complete Flow Diagrams](#complete-flow-diagrams)
- [👥 User Roles & Workflow](#user-roles--workflow)
- [🛠️ Tech Stack](#tech-stack)
- [📦 Installation & Setup](#installation--setup)
- [🚀 Running the Application](#running-the-application)
- [📝 API Endpoints](#api-endpoints)
- [🔐 Security](#security)
- [🔍 Troubleshooting](#troubleshooting)
- [📁 Project Structure](#project-structure)
- [🧪 Testing](#testing)
- [🚧 Future Enhancements](#future-enhancements)

---

## 🚀 Quick Start

### 1. Prerequisites (Check These First)
```bash
node --version          # Should be Node.js v16+
python --version        # Should be Python 3.8+
docker --version        # For MongoDB
```

### 2. Install Everything
```bash
# Node dependencies
npm install

# Python dependencies
pip install -r requirements.txt
```

### 3. Start Services (Open 4 Terminals)

**Terminal 1 - MongoDB:**
```bash
docker run -d -p 27017:27017 --name fentam-mongo mongo:latest
```

**Terminal 2 - Hardhat Blockchain:**
```bash
npx hardhat node
```

**Terminal 3 - FastAPI Backend:**
```bash
python main.py
# Runs on http://localhost:8000
```

**Terminal 4 - Streamlit Frontend:**
```bash
cd streamlit_app
streamlit run streamlit_app.py
# Runs on http://localhost:8501
```

### 4. Access the App
- **Frontend**: http://localhost:8501
- **Backend API**: http://localhost:8000
- **Swagger Docs**: http://localhost:8000/docs

### 5. Test Login
```
Email: admin@fentam.com (or any email for signup)
Role: manufacturer/distributor/retailer/pharmacy/admin
```

---

## 🎯 Project Overview

## 🎯 Project Overview

**What is FENTAM?**
- ✅ Blockchain-based pharmaceutical supply chain tracking
- ✅ Prevents fentanyl product misplacement
- ✅ Ensures complete transparency & accountability
- ✅ Multi-tier admin approval workflow
- ✅ Immutable record keeping
- ✅ Real-time location tracking

**Who Uses It?**
- **Manufacturers**: Create drug batches
- **Distributors**: Handle product logistics
- **Retailers**: Manage inventory
- **Pharmacies**: Dispense to consumers
- **Admins**: Approve & verify all transactions

**Key Benefits**
✅ Prevents counterfeiting and diversion  
✅ Complete audit trail of every transaction  
✅ Role-based access control  
✅ Immutable blockchain records  
✅ Real-time tracking through supply chain  
✅ Admin verification at every step  

---

## 🏗️ System Architecture

### Complete System Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    FENTAM SUPPLY CHAIN SYSTEM                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              Streamlit Frontend (Web UI)                  │   │
│  │  ┌────────────────────────────────────────────────────┐  │   │
│  │  │  Authentication Layer (Login/Signup)               │  │   │
│  │  │  ├─ Manufacturer Dashboard                         │  │   │
│  │  │  ├─ Distributor Dashboard                          │  │   │
│  │  │  ├─ Retailer Dashboard                             │  │   │
│  │  │  ├─ Pharmacy Dashboard                             │  │   │
│  │  │  └─ Admin Approval Panel                           │  │   │
│  │  └────────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────┘   │
│                           │                                       │
│                           ▼                                       │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │           FastAPI Backend (main.py)                      │   │
│  │  ┌────────────────────────────────────────────────────┐  │   │
│  │  │  /api/auth/signup         - User Registration     │  │   │
│  │  │  /api/auth/login          - User Authentication   │  │   │
│  │  │  /api/auth/pending        - Pending Users         │  │   │
│  │  │  /api/auth/approve/{id}   - Admin Approval        │  │   │
│  │  │  /api/tx/submit           - Submit Transaction    │  │   │
│  │  │  /api/tx/pending          - Pending Transactions  │  │   │
│  │  │  /api/tx/approve/{id}     - Approve Transaction   │  │   │
│  │  └────────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────┘   │
│                           │                                       │
│           ┌───────────────┼───────────────┐                      │
│           ▼               ▼               ▼                      │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐    │
│  │    MongoDB      │  │    Hardhat      │  │  Web3 Layer  │    │
│  │   (User Data)   │  │   Local Node    │  │   Contracts  │    │
│  │                 │  │                 │  │              │    │
│  │ • Users         │  │ • Blockchain    │  │ Smart        │    │
│  │ • Transactions  │  │ • Accounts      │  │ Contracts    │    │
│  │ • Approvals     │  │ • State         │  │              │    │
│  └─────────────────┘  └─────────────────┘  └──────────────┘    │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Complete Flow Diagrams

### 1️⃣ User Registration & Approval Flow

```
START: User Signup
  │
  ▼
┌─────────────────────────────────────┐
│  User fills registration form:      │
│  • Name                             │
│  • Email                            │
│  • Role (Manufacturer/Distributor)  │
│  • Wallet Address                   │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  POST /api/auth/signup              │
│  Backend creates user in MongoDB    │
│  Status: approved = false           │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  ⏳ PENDING APPROVAL                │
│  User appears in Admin Panel        │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  Admin reviews in /pages/admin.py   │
│  Clicks [APPROVE] button            │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  POST /api/auth/approve/{id}        │
│  MongoDB: approved = true           │
│  Status: ✅ APPROVED               │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  User can now LOGIN                 │
│  POST /api/auth/login               │
│  Email: "john@pharmacy.com"         │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  ✅ Success!                        │
│  Redirected to role dashboard       │
│  (pages/pharmacy.py)                │
└─────────────────────────────────────┘
```

### 2️⃣ Drug Creation & Blockchain Flow

```
MANUFACTURER DASHBOARD
  │
  ▼
┌─────────────────────────────────────┐
│  Manufacturer enters:               │
│  • Drug Name: "Fentanyl 50mcg"      │
│  • Clicks: "Submit Request"         │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  POST /api/tx/submit                │
│  {                                   │
│    actionType: "createDrug",        │
│    payload: "Fentanyl 50mcg",       │
│    requestedBy: "0x111..."          │
│  }                                   │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  FastAPI creates transaction        │
│  Saves to MongoDB                   │
│  Status: approved = false           │
│  Transaction ID: 1                  │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  ⏳ PENDING ADMIN APPROVAL          │
│  Shows in Admin Dashboard           │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  Admin clicks [APPROVE]             │
│  POST /api/tx/approve/1             │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  SMART CONTRACT EXECUTES:           │
│  function approveRequest(1) {       │
│    _createDrugFromPayload(          │
│      "Fentanyl 50mcg",              │
│      0x111...                       │
│    )                                │
│  }                                   │
│                                      │
│  ▼ INTERNAL EXECUTION ▼             │
│                                      │
│  • drugCount = 1                    │
│  • drugs[1] = {                     │
│      id: 1,                         │
│      name: "Fentanyl 50mcg",        │
│      manufacturer: "Verified...",   │
│      timestamp: now(),              │
│      currentOwner: 0x111...         │
│    }                                │
│  • emit DrugCreated(1, ...)         │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  ✅ BLOCKCHAIN SUCCESS              │
│  • Drug #1 created                  │
│  • Immutable record stored          │
│  • Event emitted                    │
│  • Ready for transfer               │
└─────────────────────────────────────┘
```

### 3️⃣ Drug Transfer Flow

```
MANUFACTURER HAS DRUG #1
  │
  ▼
┌─────────────────────────────────────┐
│  Manufacturer enters:               │
│  • Drug ID: 1                       │
│  • Distributor Wallet:              │
│    0x222...                         │
│  • Clicks: "Transfer Drug"          │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  Frontend creates payload:          │
│  payload = "1,0x222..."             │
│            (drugId,newOwner)        │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  POST /api/tx/submit                │
│  {                                   │
│    actionType: "transfer",          │
│    payload: "1,0x222...",           │
│    requestedBy: "0x111..."          │
│  }                                   │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  ⏳ PENDING ADMIN APPROVAL          │
│  Admin sees in panel                │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  Admin clicks [APPROVE]             │
│  POST /api/tx/approve/2             │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  SMART CONTRACT EXECUTES:           │
│  function approveRequest(2) {       │
│    _transferDrugFromPayload(        │
│      "1,0x222...",                  │
│      0x111...                       │
│    )                                │
│  }                                   │
│                                      │
│  ▼ INTERNAL EXECUTION ▼             │
│                                      │
│  BEFORE:                            │
│  drugs[1].currentOwner = 0x111...   │
│  (Manufacturer)                     │
│                                      │
│  VERIFICATION:                      │
│  ✓ Drug exists                      │
│  ✓ currentOwner == sender           │
│                                      │
│  AFTER:                             │
│  drugs[1].currentOwner = 0x222...   │
│  (Distributor)    ◄─── NEW OWNER    │
│                                      │
│  • emit DrugTransferred(1, ...)     │
└─────────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────────┐
│  ✅ TRANSFER COMPLETE               │
│  • Distributor now owns Drug #1     │
│  • Immutable record created         │
│  • Event logged on blockchain       │
│  • Ready for next transfer          │
└─────────────────────────────────────┘
```

### 4️⃣ Complete Supply Chain Journey

```
START: Manufacturing
│
├─ STEP 1: Manufacturer creates Drug #1 (Fentanyl 50mcg)
│          Admin approves → Drug stored on blockchain
│          Owner: Manufacturer (0x111...)
│
├─ STEP 2: Manufacturer transfers to Distributor
│          Admin approves → Ownership transferred
│          Owner: Distributor (0x222...)
│
├─ STEP 3: Distributor transfers to Retailer
│          Admin approves → Ownership transferred
│          Owner: Retailer (0x333...)
│
├─ STEP 4: Retailer transfers to Pharmacy
│          Admin approves → Ownership transferred
│          Owner: Pharmacy (0x444...)
│          Status: Ready for dispensing
│
▼
END: Pharmacy dispenses to patient

IMMUTABLE BLOCKCHAIN RECORD:
  ✓ DrugCreated(1, "Fentanyl 50mcg", 0x111...) - Timestamp: T1
  ✓ DrugTransferred(1, 0x111..., 0x222...) - Timestamp: T2
  ✓ DrugTransferred(1, 0x222..., 0x333...) - Timestamp: T3
  ✓ DrugTransferred(1, 0x333..., 0x444...) - Timestamp: T4
  
AUDIT TRAIL: Complete, transparent, unmodifiable
```

---

## 👥 User Roles & Workflow

| Role | Dashboard | Capabilities | Approval Required |
|------|-----------|--------------|------------------|
| **Manufacturer** | pages/manufacturer.py | Create drug batches, initiate transfers | ✅ Admin approval |
| **Distributor** | pages/distributor.py | Receive drugs, transfer to retailers | ✅ Admin approval |
| **Retailer** | pages/retailer.py | Receive drugs, transfer to pharmacies | ✅ Admin approval |
| **Pharmacy** | pages/pharmacy.py | Receive drugs, dispense to consumers | ✅ Admin approval |
| **Admin** | pages/admin.py | Approve users & transactions | ❌ None (authority) |

### Role-Based Authentication Flow

```
Login Page (streamlit_app.py)
  │
  ├─ Email: john@pharmacy.com
  └─ Click Login
      │
      ▼
  POST /api/auth/login
      │
      ▼
  Backend verifies email in MongoDB
      │
      ├─ NOT FOUND/NOT APPROVED → Error
      │
      └─ FOUND & APPROVED → Return user data
          {
            name: "John",
            role: "pharmacy",
            walletAddress: "0x444...",
            approved: true
          }
          │
          ▼
      Streamlit redirects to:
      pages/pharmacy.py ✓
      
  Similar routing for:
  - role: "manufacturer" → pages/manufacturer.py
  - role: "distributor" → pages/distributor.py
  - role: "retailer" → pages/retailer.py
  - role: "admin" → pages/admin.py
```

---

## 🛠️ Tech Stack

### Frontend
- **Streamlit** - Multi-page web application framework
- **Altair** - Data visualization & charts
- **Requests** - HTTP client for API calls
- **Session State** - User session management

### Backend
- **FastAPI** - High-performance Python API framework
- **Pydantic** - Data validation with models
- **MongoDB** - NoSQL database (user & transaction storage)
- **Web3.py** - Ethereum blockchain interaction

### Blockchain & Smart Contracts
- **Solidity 0.8.28** - Smart contract language
- **Hardhat** - Ethereum development environment
- **Hardhat Node** - Local Ethereum blockchain (20 pre-funded accounts)
- **Web3 Provider** - HTTP connection to blockchain

### Dependencies
See `requirements.txt` and `package.json` for complete list.

---

## 📦 Installation & Setup

### Step 1: Prerequisites
Ensure you have installed:
- **Node.js v16+** - `node --version`
- **Python 3.8+** - `python --version`
- **Docker** - `docker --version`

### Step 2: Clone & Install Dependencies

```bash
# Clone repository
git clone <repository-url>
cd Blockchain_Fentam

# Install Node packages
npm install

# Install Python packages
pip install -r requirements.txt
```

### Step 3: Setup MongoDB

**Option A: Using Docker (Recommended)**
```bash
docker run -d -p 27017:27017 --name fentam-mongo mongo:latest
```

**Option B: Local MongoDB**
```bash
# macOS with Homebrew
brew services start mongodb-community

# Or manually
mongod
```

### Step 4: Create Environment File

Create `.env` in project root:
```env
MONGO_URI=mongodb://localhost:27017/
```

### Step 5: Deploy Smart Contract

```bash
# Terminal 1: Start Hardhat node
npx hardhat node

# Terminal 2: Deploy contract (in another terminal)
npx hardhat run scripts/deploy.js --network localhost
```

Contract address will be saved to:
```
streamlit_app/contract_info.json
```

---

## 🚀 Running the Application

After setup is complete, start services in 4 separate terminals:

### Terminal 1: MongoDB (if using Docker)
```bash
# Already running from installation, verify with:
docker ps | grep mongo
```

### Terminal 2: Hardhat Blockchain Node
```bash
npx hardhat node
# Output shows 20 accounts with 10000 ETH each
# Node runs on http://127.0.0.1:8545
```

### Terminal 3: FastAPI Backend
```bash
python main.py
# Backend API: http://localhost:8000
# Swagger Docs: http://localhost:8000/docs
```

### Terminal 4: Streamlit Frontend
```bash
cd streamlit_app
streamlit run streamlit_app.py
# Frontend: http://localhost:8501
```

### Access the Application
- **Web UI**: http://localhost:8501
- **API Documentation**: http://localhost:8000/docs
- **Blockchain**: http://127.0.0.1:8545

---

## 📝 API Endpoints

### Authentication Endpoints

#### 1. User Registration
```bash
POST /api/auth/signup
Content-Type: application/json

{
  "name": "John Smith",
  "email": "john@pharmacy.com",
  "role": "pharmacy",
  "walletAddress": "0x444..."
}

Response: 200
{
  "message": "Signup successful. Awaiting admin approval."
}
```

#### 2. User Login
```bash
POST /api/auth/login
Content-Type: application/json

{
  "email": "john@pharmacy.com"
}

Response: 200
{
  "_id": "ObjectId...",
  "name": "John Smith",
  "email": "john@pharmacy.com",
  "role": "pharmacy",
  "address": "0x444...",
  "approved": true
}
```

#### 3. Get Pending Users (Admin Only)
```bash
GET /api/auth/pending

Response: 200
[
  {
    "_id": "ObjectId...",
    "name": "Jane Doe",
    "email": "jane@manufacturer.com",
    "role": "manufacturer",
    "approved": false
  }
]
```

#### 4. Approve User (Admin Only)
```bash
POST /api/auth/approve/{user_id}

Response: 200
{
  "message": "User approved successfully"
}
```

### Transaction Endpoints

#### 1. Submit Transaction (Create or Transfer)
```bash
POST /api/tx/submit
Content-Type: application/json

# For Drug Creation:
{
  "actionType": "createDrug",
  "payload": "Fentanyl 50mcg Patch",
  "requestedBy": "0x111..."
}

# For Drug Transfer:
{
  "actionType": "transfer",
  "payload": "1,0x222...",
  "requestedBy": "0x111..."
}

Response: 200
{
  "message": "Transaction submitted for approval",
  "transactionId": 1
}
```

#### 2. Get Pending Transactions (Admin Only)
```bash
GET /api/tx/pending

Response: 200
[
  {
    "_id": "ObjectId...",
    "id": 1,
    "actionType": "createDrug",
    "payload": "Fentanyl 50mcg",
    "requestedBy": "0x111...",
    "approved": false
  }
]
```

#### 3. Approve Transaction (Admin Only)
```bash
POST /api/tx/approve/{transaction_id}

Response: 200
{
  "message": "Transaction approved and executed",
  "txHash": "0xabc123..."
}
```

---

## 🔐 Security

### Smart Contract Security
✅ **Owner Verification** - Only current owner can transfer drug  
✅ **Payload Validation** - Strict format checking for payloads  
✅ **Address Parsing** - Safe hex address conversion  
✅ **Admin-Only Functions** - `approveRequest()` restricted to admin  

### Role-Based Access Control (RBAC)
✅ **Role Enforcement** - Dashboard access by role  
✅ **Approval Workflow** - All actions need admin approval  
✅ **User Status** - Must be approved before login  

### Blockchain Security
✅ **Immutable Records** - No modifications after approval  
✅ **Event Logging** - Complete audit trail  
✅ **Ownership Transfer** - Verified before state change  

### Database Security
✅ **Unique Emails** - No duplicate registrations  
✅ **Status Tracking** - Approved flag enforcement  
✅ **Timestamps** - All actions time-stamped  

---

## 🔍 Troubleshooting

### Issue 1: "Web3 not connected!"
**Cause**: Hardhat node not running  
**Solution**:
```bash
# Terminal: Start Hardhat node
npx hardhat node
```

### Issue 2: "MongoDB connection failed"
**Cause**: MongoDB not running  
**Solution**:
```bash
# Using Docker
docker run -d -p 27017:27017 mongo:latest

# Or check if already running
docker ps | grep mongo
```

### Issue 3: "Could not reach backend"
**Cause**: FastAPI not running or port blocked  
**Solution**:
```bash
# Check if port 8000 is in use
lsof -i :8000

# Kill process on port 8000
lsof -ti :8000 | xargs kill -9

# Start backend
python main.py
```

### Issue 4: "Contract not found at address"
**Cause**: Smart contract not deployed  
**Solution**:
```bash
# Ensure Hardhat node is running, then:
npx hardhat run scripts/deploy.js --network localhost
```

### Issue 5: "Port 8501 already in use"
**Cause**: Streamlit already running  
**Solution**:
```bash
# Kill process on port 8501
lsof -ti :8501 | xargs kill -9

# Start Streamlit again
cd streamlit_app
streamlit run streamlit_app.py
```

### Debug Commands

```bash
# Check Hardhat node connection
curl http://127.0.0.1:8545

# Check FastAPI backend
curl http://localhost:8000/docs

# Check MongoDB connection
mongo mongodb://localhost:27017/

# View MongoDB data
# Use MongoDB Compass → mongodb://localhost:27017
# Database: fentam
# Collections: users, txrequests

# Check running containers
docker ps

# View logs
docker logs fentam-mongo
```

---

## 📁 Project Structure

```
Blockchain_Fentam/
│
├── 📄 contracts/
│   └── FentanylSupplyChain.sol     # Smart contract (Solidity)
│                                    # • Drug struct & storage
│                                    # • submitRequest() function
│                                    # • approveRequest() function
│                                    # • Transfer & creation logic
│
├── 📄 scripts/
│   ├── deploy.js                   # Contract deployment script
│   └── init_users.js               # Initialize test data
│
├── 📄 streamlit_app/               # Main Streamlit frontend
│   ├── streamlit_app.py            # Login & route dispatcher
│   ├── web3_helpers.py             # Web3 & MongoDB utilities
│   ├── login.py                    # Authentication logic
│   ├── contract_info.json          # Deployed contract address
│   ├── pages/
│   │   ├── admin.py                # Admin approval dashboard
│   │   ├── admin_dashboard.py      # Extended admin panel
│   │   ├── manufacturer.py         # Create drugs, initiate transfers
│   │   ├── distributor.py          # Receive & transfer drugs
│   │   ├── retailer.py             # Manage inventory
│   │   ├── pharmacy.py             # Final dispensing point
│   │   └── register.py             # User registration page
│   └── artifacts/                  # Compiled contract ABIs
│
├── 📄 main.py                      # FastAPI backend
├── 📄 transactions.py              # Transaction utilities
├── 📄 hardhat.config.js            # Hardhat configuration
│
├── 📄 package.json                 # Node dependencies
├── 📄 requirements.txt             # Python dependencies
├── 📄 README.md                    # This file
│
├── 📁 test/                        # Test files
├── 📁 artifacts/                   # Compiled contracts
├── 📁 cache/                       # Build cache
├── 📁 ignition/                    # Hardhat ignition modules
│
└── 📄 .env                         # Environment variables
```

### Key File Descriptions

| File | Purpose |
|------|---------|
| `contracts/FentanylSupplyChain.sol` | Core blockchain logic |
| `main.py` | FastAPI backend with 7 endpoints |
| `streamlit_app/streamlit_app.py` | Frontend entry point & login |
| `streamlit_app/web3_helpers.py` | Blockchain & DB connections |
| `streamlit_app/pages/*.py` | Role-specific dashboards |
| `scripts/deploy.js` | Deploys contract & saves address |

---

## 🧪 Testing

### Run Smart Contract Tests
```bash
npx hardhat test
```

### Run with Gas Report
```bash
REPORT_GAS=true npx hardhat test
```

### Test with Sample Data

**Hardhat Node Accounts** (auto-generated, 10000 ETH each):
```
Account 0: 0x0000000000000000000000000000000000000001
Account 1: 0x0000000000000000000000000000000000000002
... (20 total accounts)
```

**Test Workflow**:
1. Signup as Manufacturer
2. Admin approves signup
3. Manufacturer creates drug
4. Admin approves drug creation
5. Manufacturer transfers to Distributor
6. Admin approves transfer
7. Verify ownership on blockchain

---

## 📊 Smart Contract Functions Reference

### `submitRequest(actionType, payload)`
Submits a request for processing (drug creation or transfer).

**Parameters:**
- `actionType` (string): "createDrug" or "transfer"
- `payload` (string): Drug name or "{drugId},{newOwnerAddress}"

**Returns:**
- Event: `RequestSubmitted`

**Example:**
```solidity
submitRequest("createDrug", "Fentanyl 50mcg")
submitRequest("transfer", "1,0x222...")
```

### `approveRequest(requestId)`
Admin-only function to approve and execute requests.

**Parameters:**
- `requestId` (uint): ID of request to approve

**Modifiers:**
- `onlyAdmin`: Only contract admin can call

**Actions:**
- Validates request exists
- Executes appropriate function (create or transfer)
- Emits `RequestApproved` event
- Updates blockchain state

**Example:**
```solidity
approveRequest(1)  // Approves request #1
```

### `getCurrentOwner(drugId)`
Query the current owner of a drug.

**Parameters:**
- `drugId` (uint): ID of drug

**Returns:**
- `address`: Current owner's wallet address

**Example:**
```solidity
address owner = getCurrentOwner(1)
// Returns: 0x222... (or current owner)
```

### Events

```solidity
event RequestSubmitted(uint id, string actionType, string payload, address requestedBy)
event RequestApproved(uint id)
event DrugCreated(uint id, string name, address owner)
event DrugTransferred(uint id, address from, address to)
```

---

## 📝 Data Models

### User Document (MongoDB)
```json
{
  "_id": "ObjectId",
  "name": "John Smith",
  "email": "john@pharmacy.com",
  "role": "pharmacy",
  "address": "0x444...",
  "approved": true,
  "timestamp": "2026-02-15T10:30:00Z"
}
```

### Transaction Request (MongoDB)
```json
{
  "_id": "ObjectId",
  "id": 1,
  "actionType": "createDrug",
  "payload": "Fentanyl 50mcg",
  "requestedBy": "0x111...",
  "approved": true,
  "timestamp": "2026-02-15T10:32:00Z"
}
```

### Drug (On Blockchain)
```solidity
struct Drug {
  uint id;
  string name;
  string manufacturer;
  uint timestamp;
  address currentOwner;
}

// Example:
{
  id: 1,
  name: "Fentanyl 50mcg Patch",
  manufacturer: "Verified Manufacturing Co.",
  timestamp: 1708009200,
  currentOwner: "0x444..."
}
```

---

## 🚧 Future Enhancements

- 🔲 QR code generation for physical product tracking
- 🔲 Real-time push notifications for transactions
- 🔲 Advanced analytics dashboard
- 🔲 Integration with mainnet Ethereum
- 🔲 Mobile application (React Native)
- 🔲 Automated recall system
- 🔲 Consumer verification portal
- 🔲 AI-based fraud detection
- 🔲 IoT sensor integration
- 🔲 Multi-signature approvals

---

## 📊 Key Features

✅ **Immutable Drug Records** - Stored permanently on blockchain  
✅ **Role-Based Access Control** - Different dashboards per role  
✅ **Admin Approval Workflow** - Two-tier verification process  
✅ **Real-Time Tracking** - Track drugs through entire supply chain  
✅ **Event Logging** - Complete audit trail of all transactions  
✅ **User Management** - MongoDB-based scalable user storage  
✅ **Transaction History** - Complete blockchain history  
✅ **Decentralized Verification** - Smart contract-based verification  

---

## 📄 License

ISC

## 👥 Contributors

FENTAM Supply Chain Management Team

## 📞 Support & Documentation

For issues or detailed documentation:
- Check **Troubleshooting** section above
- Review code comments in key files
- Check Hardhat node console for blockchain events
- Use MongoDB Compass to inspect database

---

**Project Status**: ✅ Production Ready  
**Version**: 1.0.0  
**Last Updated**: February 15, 2026  
**Maintained By**: Development Team
