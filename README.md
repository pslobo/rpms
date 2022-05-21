# Command Line Tools

This repo contains rpm specs for several tools that are either missing or outdated in the official fedora repositories.

While this is a personal repo for tools I need and targeted at the CPU architectures I own, PRs are welcome for additional tools and architectures.

The corresponding [Copr repository](https://copr.fedorainfracloud.org/coprs/plobo/tools/). Enable with `dnf copr enable plobo/tools`.

## Included packages

| Package                                               | Build status                                                                                                                                                                                      |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`k9s`](https://github.com/derailed/k9s)              | [![Copr build status](https://copr.fedorainfracloud.org/coprs/plobo/tools/package/k9s/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/plobo/tools/package/k9s/)             |
| [`aws-vault`](https://github.com/99designs/aws-vault) | [![Copr build status](https://copr.fedorainfracloud.org/coprs/plobo/tools/package/aws-vault/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/plobo/tools/package/aws-vault/) |

## Credits

* k9s: Initial spec from [Claudi](https://git.chaoslama.org/claudi/rpms/src/branch/main/k9s.spec)
* aws-vault: Initial spec from []
