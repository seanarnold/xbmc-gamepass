## Auth
POST: https://gamepass.nfl.com/secure/authenticate
Payload:

```
{
  username: <username>,
  password: <password>,
  format: 'json',
  accesstoken: true
}
```

Response:

```
{
  "code": "loginsuccess",
  "data": {
    "firstName": "<username>",
    "hasFreeTrial": "true",
    "trackUsername": "<id>",
    "wasFreeTrial": "true",
    "locale": "en_US",
    "accessToken": "<token>",
    "hasSubscription": "true",
    "username": "<username>"
  }
}
```


## Get schedules

GET: https://nflapi.neulion.com/api_nfl/v1/schedule?format=json
Headers: "Authorization: Bearer token"

Params:

```
week: 2,
season: 2017,
gametype: 1,
format: json
```
```
Gametype For schedules:
1: Preaseaon
2: Regular Season
3: Playoffs
```

Respone: 

```
{
  "currentDate": "2017-08-18T19:31:41.337",
  "season": "2017",
  "gameType": "1",
  "week": "2",
  "paging": {
    "pageNumber": 1,
    "totalPages": 1,
    "count": 16,
    "navStart": 1,
    "navEnd": 1
  },
  "games": [
    {
      "id": "37186",
      "extId": "2017081753",
      "seoName": "bills-at-eagles-on-08172017",
      "date": "2017-08-17T19:00:11.000",
      "dateTimeGMT": "2017-08-17T23:00:11.000",
      "endDateTimeGMT": "2017-08-18T02:32:16.000",
      "image": "",
      "logo": ".png",
      "leagueId": "",
      "sportId": "",
      "sportName": "",
      "season": "2017",
      "week": "2",
      "type": "1",
      "name": "",
      "location": "",
      "isGame": "true",
      "result": "F",
      "awayTeam": {
        "id": "5",
        "name": "Bills",
        "score": "16",
        "code": "BUF"
      },
      "homeTeam": {
        "id": "30",
        "name": "Eagles",
        "score": "20",
        "code": "PHI"
      },
      "gameState": 3,
      "availablePrograms": 9,
      "accessSkus": [
        "GPREMIUM"
      ],
      "blackoutStations": "Local Game",
      "statsId": "57194"
    },
    ...
  ]
}
```

## Get Stream URL
POST: https://nflapi.neulion.com/api_nfl/v1/publishpoint

or;

https://gamepass.nfl.com/service/publishpoint

The former seems to be blackouting some games for International users which seems to be a bug.

Headers: "Authorization: Bearer token"
Payload:

```
pcid: ?? (doesn't seem to be needed),
id: game_id (i.e 37186),
gs: game_state,
nt: 1, (not sure what this is)
gt: game_type,
type: game
```

```
game_type:
1: Games
8: Condensed game

```

Example: 

```
format: json,
id: 37186
gs: 3
nt: 1
gt: 1
type: game
```

Response: 

```
{
	"path": "m3u8_url",
	"pcmToken": "pcm_token"
}
```

## Get Stream Options

GET: m3u8_url URL from above call

Response: 

```
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=400000,CODECS="avc1.4D400D,mp4a.40.2",RESOLUTION=400x224
1_37186_buf_phi_2017_b_whole_1_400_iphone.mp4.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=4500000,CODECS="avc1.4D4028,mp4a.40.2",RESOLUTION=1920x1080
1_37186_buf_phi_2017_b_whole_1_4500_iphone.mp4.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=3000000,CODECS="avc1.4D4020,mp4a.40.2",RESOLUTION=1280x720
1_37186_buf_phi_2017_b_whole_1_3000_iphone.mp4.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2400000,CODECS="avc1.4D401F,mp4a.40.2",RESOLUTION=960x540
1_37186_buf_phi_2017_b_whole_1_2400_iphone.mp4.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1600000,CODECS="avc1.4D401F,mp4a.40.2",RESOLUTION=960x540
1_37186_buf_phi_2017_b_whole_1_1600_iphone.mp4.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1200000,CODECS="avc1.4D401E,mp4a.40.2",RESOLUTION=640x360
1_37186_buf_phi_2017_b_whole_1_1200_iphone.mp4.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=800000,CODECS="avc1.4D401E,mp4a.40.2",RESOLUTION=640x360
1_37186_buf_phi_2017_b_whole_1_800_iphone.mp4.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=240000,CODECS="avc1.4D400D,mp4a.40.2",RESOLUTION=400x224
1_37186_buf_phi_2017_b_whole_1_240_iphone.mp4.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=150000,CODECS="avc1.4D400D,mp4a.40.2",RESOLUTION=400x224
1_37186_buf_phi_2017_b_whole_1_150_iphone.mp4.m3u8
```

