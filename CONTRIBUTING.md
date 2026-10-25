# Contributing

Thank you for helping. This list is organized by device model, so start from the device.

## What to add

Add a project if all of these are true:

- It customizes a specific consumer device (or device family) that the owner has.
- It is legal to use on your own device: open firmware, local control, add-on apps, configuration files, recipes, or compatible accessories.
- It is on GitHub and had a push in the last 3 years. It is not archived.

Do not add projects for DRM removal, license key or paywall bypass, piracy, game ROMs, account sharing, or carrier unlock bypass.
Projects that unlock your own device (for example a jailbreak) need the `review` flag. Link the project page only. Do not add steps.

## How to add a project

1. Edit `data/devices.yaml`. Find the device model, or add a new model under the correct category.
2. Add an entry with `name`, `repo` (`owner/name`), `summary` (one English sentence in your own words), `summary_zh` (Traditional Chinese), and `flags`.
   Set `stars: 0`, `pushed: TODO`, and `license: TODO`. The script fills them in.
3. Use these flags when they apply:
   - `mains`: the device has mains voltage inside.
   - `opens`: you must open the device or solder.
   - `warranty`: it likely voids the warranty.
   - `review`: it unlocks the device.
4. Run the scripts (Python 3 standard library and a logged-in `gh` CLI):

   ```sh
   cd scripts
   python3 refresh.py   # stars, last push, and license from the GitHub API
   python3 build.py     # README.md and README.zh-TW.md
   python3 check.py     # fields, URLs, and API facts
   ```

5. Do not edit `README.md` or `README.zh-TW.md` by hand. Commit the YAML and both generated files.
