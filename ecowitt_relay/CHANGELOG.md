# Changelog

## [2.1.0] - 2025-04-06
- God dammit chatgpt...pressure is fixed.

## [2.0.2] - 2025-04-06
- Continue to clean up logging.

## [2.0.1] - 2025-04-06
### Changed
- **Cleaned up logging:** stop logging HTML

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

