class SecurityReport:

    def generate(self, result):
        report = []

        report.append("=" * 50)
        report.append("          PASSWORD SECURITY AUDIT REPORT")
        report.append("=" * 50)

        status = "PASS" if result["valid"] else "FAIL"

        report.append(f"Password Status   : {status}")
        report.append(f"Strength          : {result['strength']}")
        report.append(f"Entropy           : {result['entropy']:.2f} bits")

        common = "YES" if result["is_common"] else "NO"
        pattern = "YES" if result["has_pattern"] else "NO"
        keyboard = "YES" if result["has_keyboard_pattern"] else "NO"

        report.append(f"Common Password   : {common}")
        report.append(f"Common Pattern    : {pattern}")
        report.append(f"Keyboard Pattern  : {keyboard}")

        report.append("")
        report.append("Policy Issues:")

        if result["errors"]:
            for error in result["errors"]:
                report.append(f"- {error}")
        else:
            report.append("None")

        report.append("")
        report.append("Security Summary:")

        if result["valid"]:
            report.append(
                "Password satisfies the configured security policy."
            )
        else:
            report.append(
                "Password does not satisfy the configured security policy."
            )

        report.append("=" * 50)

        return "\n".join(report)