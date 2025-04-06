# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-04-06
### New
- **OMG PRESSURE WORKS NOW**
### Changed
- **Cleaned up logging:** should only log on failures now.

## [1.3] - 2025-04-06
### Changed
- **PWS API URL Updated:** Changed the forwarding URL to use the current endpoint:
  `http://pwsweather.com/pwsupdate/pwsupdate.php`
- **Parameter Mapping:** Converted the Ecowitt data into Weather Underground formatting before sending to the PWS API.
- **Logging:** Added logging to output the final URL with all parameters for debugging purposes.

