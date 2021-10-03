
Convert Google Authenticator export QR code to one qr per OTP

## Install

### MacOS

```bash
brew install poetry
brew install zbar
poetry install
```


## Usage

Run the cli tool and hold the GAuth export QR code to the camera:

```bash
gauth_exporter
```

The QR codes will be placed inside `qrs/` directory, scan them as usual to add them to your OTP of choice.
