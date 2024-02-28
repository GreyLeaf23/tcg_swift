// Import the TCGdex SDK
const TCGdex = require('@tcgdex/sdk').default;

// Instantiate the SDK
const tcgdex = new TCGdex('en');

// Use the SDK within an async function
(async () => {
    try {
        const card = await tcgdex.fetch('cards', 'swsh3-136');
        console.log(card);
    } catch (error) {
        console.error(error);
    }
})();
