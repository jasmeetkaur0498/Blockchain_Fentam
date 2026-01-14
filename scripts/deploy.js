const fs = require("fs");
const path = require("path");

async function main() {
  const FentanylSupplyChain = await ethers.getContractFactory("FentanylSupplyChain");
  const contract = await FentanylSupplyChain.deploy();

  await contract.waitForDeployment();
  const address = await contract.getAddress();

  console.log(" Contract deployed to:", address);

  // Save contract address to file
  const contractInfo = {
    address,
  };

  fs.writeFileSync(
    path.resolve(__dirname, "../contract_info.json"),
    JSON.stringify(contractInfo, null, 2)
  );
  console.log("📦 Contract info written to contract_info.json");
}

main().catch((error) => {
  console.error(" Deployment error:", error);
  process.exit(1);
});
