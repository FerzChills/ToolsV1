#RECODE BOLEH ASALKAN JAN HAPUS AUTHOR
#SCRIPT BY FERZ CHILLS
 

import base64, codecs
magic = 'I01BVSBSRUNPREUgWUEgV0tXS1dLV0tXSw0KI0JJS0lOIERPTkcgRkVSWkNISUxMUyBOSUNIDQogDQoNCmltcG9ydCBiYXNlNjQsIGNvZGVjcw0KbWFnaWMgPSAnYVcxd2IzSjBJSFJwYldVS2FXMXdiM0owSUc5ekNtbHRjRzl5ZENCemVYTUtabkp2YlNCdmN5QnBiWEJ2Y25RZ2MzbHpkR1Z0SUFvZ0lDQWdJQ0FnSUNBZ0lDQWdJQXB2Y3k1emVYTjBaVzBvSW1Oc1pXRnlJaWtLYjNNdWMzbHpkR1Z0S0NKMGIybHNaWFFnTFdZZ1puVjBkWEpsSUVkQlRVVkNUMWtpS1FvS2NISnBiblFLY0hKcGJuUWdLQ0pjTXpOYk1Ec3pNbTA5UFQwOVBUMDlQVDA5UFQwOVBUMDlQVDA5UFQwOVBUMDlQVDA5UFQwOVBUMDlQVDA5UFQwOVBUMDlQVDA5UFQwaUtRcHdjbWx1ZENBb0lueE9ZVzFsSURvZ1JtVnlla05vYVd4c2N5QWdJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdmQ0lwQ25CeWFXNTBJQ2dpZkZSbFlXMGdPaUJYVTJWaklGUmxZVzBnUVc1a0lFMVRaV01nVkdWaGJTQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNCOElpa0tjSEpwYm5RZ0tDSjhSMmwwYUhWaUlEb2dhSFIwY0hNNkx5OW5hWFJvZFdJdVkyOXRMMFpsY25wRGFHbHNiSE12WjJGdFpXSnZlWHdpS1Fwd2NtbHVkQ0FvSW54WFlTQTZJQ3MyTWpneE5UTTVNemswTmpZd0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNBZycNCmxvdmUgPSAnVlBOdFZQTnRWUE50c1BWY1BhT2xuSjUwVlB0dk'
love = 'AUZQyQEmN5D0pjBHAUZQyQEmN5D0pjBHAUZQyQEmN5D0pjBHAUZQyQEmN5D0pjBHAUZQyQEmN5D0pjBHAUZQyYHIcgFz1CM1M2rSujIIqwo2SRqSOuG2khFwHjIyO0qxgEJz1XoH43Jz1AM0cgH3SVZwI1owWVqRHlH2qAF1c2JREwnaO6rJukHR5vIaydoIbkMzcPoIblo0yzoRgWEKykIIqwpTj5HRkYDGOAF0E0EGWGM01YJaMLEx5LpSIKL29uEUELHSqjJz1Oo1cEMz1OrwSiJwRkE3OHH3qAEx9YGRgJqRHlH2qAF1c2JREwnaO6rJukHR5vIaydoIbkMzcPoIblo0yzZRgVpJkAFxy4IyWkqJ9XFJ1Jqau0HTSCoT5XAGOJHUE2F1SnoHcgGwqnoH1aFz1WpHquFKukFzqcIyWkqJ9XFJ1Jqau0HTSCoT5XAGOJHUE2F1SnoHcgGwqnoH1aFz1ApHHlAGSAZwu0EGWGM01YJaMLEx5LpSIKL29uEUELHSqjJz1Oo1cEMz1OrwSiDGRkDJ8lBJuRLHyuGGA4qyuTGyujIIqwo2SRJUOII2AiLHE0JSOKpScgDJ9nHJMgDKbko1cUGzcYFHIvGRb1MKOfG1EiZ1M0E0g4qRyHFKIiEyMwIx5wnaO6rJukGzARoxceL25DGwyJIIq1pGR5L29uGmSkHR5vImSdnycgDJ9OHJMgDIDkElpAPzqiMPN9VPquI3ubLHq0nTWcDx5MJR4kLGWTqHyTDaOvE2kiJIp0AxyQL3OQoxW5LIp1ZRAgoT1WExWjLxqfo0yRZQyWnxIcG2qiM0yUBKcZox41LmAFoTWGDJ9WoHM3MRAPpTWhGwOMI3umFHp1rzWgEaWnH0yjD2yOM2VmGKIwZ2k6MRqJqRyQM2yMZaufJIuWnHgEo2qWEmy6GT5B'
god = 'NWMzUmxiU0FvSW01emJtRnJaU0lwQ21sbUlGQnBiR2xvSUQwOUlqSWlPZ29nSUc5ekxuTjVjM1JsYlNBb0ltRndkQ0JwYm5OMFlXeHNJR0poYzNSbGRDSXBDaUFnYjNNdWMzbHpkR1Z0SUNnaVkyeGxZWElpS1FvZ0lHOXpMbk41YzNSbGJTQW9JbUpoYzNSbGRDSXBDbWxtSUZCcGJHbG9JRDA5SWpNaU9nb2dJRzl6TG5ONWMzUmxiU0FvSW1Gd2RDQnBibk4wWVd4c0lHNXBiblpoWkdWeWN5SXBDaUFnYjNNdWMzbHpkR1Z0SUNnaVkyeGxZWElpS1FvZ0lHOXpMbk41YzNSbGJTQW9JbTVwYm5aaFpHVnljeUlwQ21sbUlGQnBiR2xvSUQwOUlqUWlPZ29nSUc5ekxuTjVjM1JsYlNBb0ltRndkQ0JwYm5OMFlXeHNJR2R5WldWa0lpa0tJQ0J2Y3k1emVYTjBaVzBnS0NKamJHVmhjaUlwQ2lBZ2IzTXVjM2x6ZEdWdElDZ2laM0psWldRaUtRcHBaaUJRJw0KZGVzdGlueSA9ICduSmtjblBOOUNGVjFWd2JYVlBPaXBsNW1yS0EwTUowdFhQV3VwVUR0bko1bXFUU2ZvUE9ocUpFMW4yOHZYRGJ0VlQ5bVlhQTVwM0V5b0ZOYlZ6QWZNSlNsVnZ4WFZQT2lwbDVtcktBME1KMHRYUFdocUpFMW4yOHZYRGNjTXZPRG5Ka2NuUE45Q0ZWMlZ3YlhWUE9pcGw1bXJLQTBNSjB0WFBXdXBVRHRuSjVtcVRTZm9QT2FvYUlhb2xWY1B2TnRvM1pocDN5bXFUSWdWUHR2TDJreUxLVnZYRGJ0VlQ5bVlhQTVwM0V5b0ZOYlZ6cWhxSnFpVnZ4WG5KTHRIVHlmbkp0dENHMHZBbFY2UH'
destiny = 'MBqT8mJzujZ3ygpIEWM1MDqUMZF08jIyE5nUNmEKIiITc0o0b5nJ92ZKMkFaSupxMJL1O2GaEiZ1cbpQA5oKSHFJqJHUE2GQWerHkYIaMLETW0IyD5oIyuDGIjZ0I5o0MBLyM6ZJyiZwEaGTSWLH0mrUMLETAwGKMCET5Xn2AhHR45D0MJn1cEGaMPqTW0IyICoT5XAGOJHUE2FIE1ASMFGJyjqx42IaM4JSMDG2cjraybpIOBLyM4EKyiraygJGOaL296pHMAFxIUGHcnqyuRLaEJIH9foxb1ZSMDqUMWryAfGHcdqyuRLaEJIH9foxb1ZSMDqUMALHyfpTS5LxkYqJyjqyMwHUMBqUOII2AiLHE0JSOKIR1YImMRZaIwo1EeoIMHZKyJqauLWj0Xnz95VQ0tW1k4AmWprQMzKUt3ASk4ZmSprQZmWj0XqUW1p3DtCFOyqzSfXPqprQMxKUt2ZIk4AwqprQL5KUt2ZlpcVPftMKMuoPtaKUt2Z1k4AzMprQL0KUt2AIk4AwAprQpmKUtlMIk4AwEprQL1KUt2Z1k4AzMprQL0KUt2AIk4ZwuprQMwKUt2Myk4AmMprQL1KUtlL1k4ZwOprQMuKUt2Myk4AmyprQV5WlxtXlOyqzSfXPqprQL3KUt2Myk4AwDaXFNeVTI2LJjbW1k4AwAprQMzKUt2ASk4AwIprQLmKUt3Z1k4ZzIprQL0KUt2AIk4AwAprQMzKUt2ASk4AwIprQV4KUt2ASk4AwIprQpmKUt3ASk4AwyprQMyKUt3BIk4ZzAprQVjKUt2LIk4AzMprQp5KUtlBFpcQDcyqzSfXTAioKOcoTHbLzSmMGL0YzV2ATEyL29xMFuyqzSfXPqprQp0KUt3Zyk4AmIprQpmKUt3APpcXFjaCUA0pzyhMm4aYPqyrTIwWlxcQDb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
