"""
$clientSeed = "test";
$nonce = "1";
$serverSeed = "test";
$mines_number = 18;

$nonce_increase = 0;
$chars = 2;
$maxNumber = floor(pow(16, $chars) / 36) * 36;
$final_indexes = [];

while (!$done) {
    $seed=hash_hmac('sha512',$clientSeed .','. $nonce .'-'. $nonce_increase, $serverSeed);
    
    for ($i = 0; $i < floor(128 / $chars); $i++) {
        $number = intval(hexdec(substr($seed, $i * $chars, $chars)), 10);
        if ($number < $maxNumber) {
            $number = $number % 36;
            if (!in_array($number, $final_indexes)) {
                $final_indexes[] = $number;
                if (count($final_indexes) === $mines_number) {
                    $done = true;
                    break;
                }
            }
        }
    }
    $nonce_increase++;
}
print_r($final_indexes);
"""


import hmac
import hashlib

# These are the variables from the problem
client_seed = "CiaoYoutubeSeedSceltoDaEmotionalDataHaHa"
nonce = "4"
server_seed = "64ef50325f7a3f479f85d20bfab60d8fbbce758b3f0c8d09c6ca46fbcd8bb6f3a8b2025fe9ef3580c8d083bba3cb44bf0383b9f2261bcf60493074f62e827ef7"
mines_number = 5

nonce_increase = 0
chars = 2
max_number = (16**chars // 36) * 36
final_indexes = []
done = False

while not done:
    print()
    # Generate the seed using HMAC-SHA512
    seed_data = f"{client_seed},{nonce}-{nonce_increase}"
    seed = hmac.new(
        server_seed.encode(), seed_data.encode(), hashlib.sha512
    ).hexdigest()
    print(seed)

    #17a46eb5b84d93bc1bb5a3a6a08ac010d227212f6995334ffd47752d680dd2f41683809d0ff11e6233afd2e2f25dd1a5a98090608ec5ef06409629cacb4a9083
    # Iterate through the seed in chunks
    for i in range(len(seed) // chars):
        number_hex = seed[i * chars : (i * chars) + chars]
        number = int(number_hex, 16)

        if number < max_number:
            number = number % 36  # 0 - 35

            if number not in final_indexes:
                final_indexes.append(number)
                if len(final_indexes) == mines_number:
                    done = True
                    break
    nonce_increase += 1

print(sorted(final_indexes))

