const axios = require('axios')
async function getPhoneNumbers(country, phoneNumber) {
    const URL = 'https://jsonmock.hackerrank.com/api/countries?name='
    try {
        const result = await axios.get(`${URL}${country}`).then((response) => {
            
            return response
        })
        if (result.status !== 200) {
            throw new Error('API REQUEST FAIL')
        }
        const { data } = result.data
        
        if (!data[0]) {
            return -1
        } else {
            const code = data[0].callingCodes
            const callingCodes = code[code.length - 1]
            
            return `+${callingCodes} ${phoneNumber}`
        }
        
    } catch(e) {
        console.log(e)
    }
}