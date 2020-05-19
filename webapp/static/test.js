const secretId = 'xxx';
const secretKey = 'xxx';
const params = {
      userid: 'xx',
      instanceid: 1,
      subject: subject,
      type: 0,
      start_time: getTime(startTime).toString(),
      end_time: getTime(endTime).toString(),
      settings: {}
};

const HTTPMethod = 'POST';
const url = '/v1/meetings';
const headerString = 'X-TC-Key=' + secretId + '&X-TC-Nonce=' + randomNumber(10000, 99999) + '&X-TC-Timestamp=' + nowTime();
const stringToSign = HTTPMethod + '\n' +
      headerString + '\n' +
      url + '\n' +
      JSON.stringify(params);
const key = CryptoJS.enc.Utf8.parse(secretKey);
const content = CryptoJS.enc.Utf8.parse(stringToSign);
const hmac = CryptoJS.enc.Hex.stringify(CryptoJS.HmacSHA256(content, key));
console.log(btoa(hmac)); //签名字符串