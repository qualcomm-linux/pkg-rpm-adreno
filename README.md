# pkg-rpm-adreno

This repository has RPM packaging rules and scripts for prebuilt adreno binaries.

---

## Workflows

| Workflow | Trigger | Purpose |
|---|---|---|
| [`build-on-pr.yml`](.github/workflows/build-on-pr.yml) | Pull request | Build the RPM(s) so reviewers confirm the package still builds. Read-only — never publishes. |
| [`pkg-release.yml`](.github/workflows/pkg-release.yml) | Manual (`workflow_dispatch`) | Build **and** publish the RPM(s) to Artifactory, behind an approval gate. |

Both delegate to reusable workflows in `qcom-rpm-utils`, which run `rpmbuild`
inside the prebuilt `rpm-builder` container image for the runner's host
architecture.

---

## Branch model

This project follows the Fedora/CentOS **dist-git** convention: **one branch per
distro stream**, with the packaging files at that branch's root.

| Branch | Role | Contents |
|---|---|---|
| `main` | Template + docs home. **Nothing is built here.** | This README, [docs/](docs/), community files, workflows. |
| `c10s` | **CentOS 10 Stream package branch — where you work.** | `adreno.spec` + `sources` at the root, plus the workflows. |

Future streams get their own branch (`c11s`, …) off the same model, so one repo
can carry a package for several distro versions without branching history.

---

## Updating the package version

This is the everyday workflow — **two edits on `c10s`, no tarball in git**:

1. Bump `Version:` in the spec (and the `Source0:` URL if its path changed).
2. Recompute the checksum for the new tarball:
   ```bash
   sha512sum --tag <component>-<newversion>.tar.gz > sources
   ```
3. Commit the spec + `sources`, open a PR (build verifies it), merge, then run
   **Release**. The first release fetches the new upstream tarball, verifies it,
   and caches it back to Artifactory automatically.

### License

pkg-rpm-adreno is licensed under the [BSD-3-Clause License](https://spdx.org/licenses/BSD-3-Clause.html). See [LICENSE.txt](https://github.com/qualcomm-linux/pkg-rpm-adreno/blob/main/LICENSE.txt) for the full license text.