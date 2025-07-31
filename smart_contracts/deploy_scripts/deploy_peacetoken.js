const Web3 = require('web3');
const { abi, evm } = require('../PeaceToken.json'); // Assuming PeaceToken.json is generated from the Solidity contract

const deploy = async () => {
    const web3 = new Web3('http://localhost:8545'); // Connect to local Ethereum node
    const accounts = await web3.eth.getAccounts();

    console.log('Deploying contracts with the account:', accounts[0]);

    const result = await new web3.eth.Contract(abi)
        .deploy({ data: evm.bytecode.object })
        .send({ from: accounts[0], gas: '1000000' });

    console.log('Contract deployed to:', result.options.address);
};

deploy();