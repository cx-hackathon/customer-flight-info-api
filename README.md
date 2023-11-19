# Customer Flight Info API

- An integration of Cathay's API and our mock database

<!-- vscode-markdown-toc -->

- 1. [API Key and Database connection](#APIKeyandDatabaseconnection)
- 2. [Hostname](#Hostname)
- 3. [Customer Details API](#CustomerDetailsAPI)
  - 3.1. [Endpoint](#Endpoint)
  - 3.2. [Method](#Method)
  - 3.3. [Path Variable](#PathVariable)
  - 3.4. [Sample Response](#SampleResponse)
- 4. [Airport Facilities API](#AirportFacilitiesAPI)
  - 4.1. [Endpoint](#Endpoint-1)
  - 4.2. [Method](#Method-1)
  - 4.3. [Path Variable](#PathVariable-1)
  - 4.4. [Query Params](#QueryParams)
  - 4.5. [Sample Response](#SampleResponse-1)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## 1. <a name='APIKeyandDatabaseconnection'></a>API Key and Database connection

| key           | token                                                     | description                    |
| ------------- | --------------------------------------------------------- | ------------------------------ |
| `API_KEY`     | `V6lY3PSPozs1RAokZYrjWeGdTxMTg91o`                        | api key for using cathay's api |
| `DB_URL`      | `cathay-db.czmjojkq9oam.ap-southeast-1.rds.amazonaws.com` | Postgresql DB host url         |
| `DB_PASSWORD` | `789906b55245`                                            | password for DB connection     |

## 2. <a name='Hostname'></a>Hostname

| hostname                             | stage |
| ------------------------------------ | ----- |
| https://dtoi798bnqwwr.cloudfront.net | prod  |

## 3. <a name='CustomerDetailsAPI'></a>Customer Details API

### 3.1. <a name='Endpoint'></a>Endpoint

> /v1/customer/:pid

where `pid` is passenger id

### 3.2. <a name='Method'></a>Method

> GET

### 3.3. <a name='PathVariable'></a>Path Variable

| name | type   | description  |
| ---- | ------ | ------------ |
| pid  | string | Passenger ID |

### 3.4. <a name='SampleResponse'></a>Sample Response

> URL: https://dtoi798bnqwwr.cloudfront.net/v1/customer/510892B0000153AC

```json
{
  "data": {
    "pid": "510892B0000153AC",
    "flights": {
      "CX025920231119HKG": {
        "from": {
          "at": {
            "date": "2023-11-19",
            "time": "23:55:00"
          },
          "airport": "HKG"
        },
        "to": {
          "at": {
            "date": "2023-11-20",
            "time": "05:00:00"
          },
          "airport": "LHR"
        }
      }
    }
  },
  "success": true,
  "message": ""
}
```

## 4. <a name='AirportFacilitiesAPI'></a>Airport Facilities API

### 4.1. <a name='Endpoint-1'></a>Endpoint

> /v1/facilities/:code?type={type}

### 4.2. <a name='Method-1'></a>Method

> GET

### 4.3. <a name='PathVariable-1'></a>Path Variable

| name | type   | description                               |
| ---- | ------ | ----------------------------------------- |
| code | string | Airport iata code (either `HKG` or `TPE`) |

### 4.4. <a name='QueryParams'></a>Query Params

| name | type   | description                                           |
| ---- | ------ | ----------------------------------------------------- |
| type | string | type of facilities (`restaurant`, `gate` or `toilet`) |

### 4.5. <a name='SampleResponse-1'></a>Sample Response

> URL: https://dtoi798bnqwwr.cloudfront.net/v1/facilities/HKG?type=toilet

```json
{
  "data": [
    {
      "facility_id": 5,
      "name": "Restroom 2",
      "opening_hour": {
        "Monday": {
          "from": "07:00:00",
          "to": "21:00:00"
        },
        "Tuesday": {
          "from": "07:00:00",
          "to": "21:00:00"
        },
        "Wednesday": {
          "from": "07:00:00",
          "to": "21:00:00"
        },
        "Thursday": {
          "from": "07:00:00",
          "to": "21:00:00"
        },
        "Friday": {
          "from": "07:00:00",
          "to": "21:00:00"
        },
        "Saturday": {
          "from": "09:00:00",
          "to": "19:00:00"
        },
        "Sunday": {
          "from": "10:00:00",
          "to": "18:00:00"
        },
        "Holidays": [
          {
            "date": "2023-01-01",
            "from": "08:00:00",
            "to": "20:00:00"
          },
          {
            "date": "2023-02-05",
            "from": "08:00:00",
            "to": "20:00:00"
          }
        ]
      }
    },
    {
      "facility_id": 6,
      "name": "Restroom 1",
      "opening_hour": {
        "Monday": {
          "from": "00:00:00",
          "to": "23:59:00"
        },
        "Tuesday": {
          "from": "00:00:00",
          "to": "23:59:00"
        },
        "Wednesday": {
          "from": "00:00:00",
          "to": "23:59:00"
        },
        "Thursday": {
          "from": "00:00:00",
          "to": "23:59:00"
        },
        "Friday": {
          "from": "00:00:00",
          "to": "23:59:00"
        },
        "Saturday": {
          "from": "00:00:00",
          "to": "23:59:00"
        },
        "Sunday": {
          "from": "00:00:00",
          "to": "23:59:00"
        },
        "Holidays": [
          {
            "date": "2023-01-01",
            "from": "08:00:00",
            "to": "20:00:00"
          },
          {
            "date": "2023-02-05",
            "from": "08:00:00",
            "to": "20:00:00"
          }
        ]
      }
    }
  ],
  "success": true,
  "message": ""
}
```
