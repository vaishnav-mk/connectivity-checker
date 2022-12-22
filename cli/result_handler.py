class DisplayResults:
    def __init__(self, results, args):
        self.results = results
        self.verbose = args.verbose
        self.status = args.status
        self.success = args.success

    def divider(self, len=20):
        print("-" * len)

    def display_results(self):
        success = []
        self.divider()

        for result in self.results:
            if result["result"]["success"]:
                success.append(result)

        if self.status:
            print(f"Filtering results by status: {self.status}")
            self.results = list(
                filter(lambda x: x["result"]["status"] in self.status, self.results)
            )
            self.divider()

        print(f"Results ({len(self.results)}):")
        self.divider()

        if self.success:
            if not success:
                print(f"No successful connections found for {len(self.results)} URLs")
            for result in success:
                return (
                    self.verbose_results(success)
                    if self.verbose
                    else print(f"Success: {result['url']}")
                )
        else:
            if self.verbose:
                self.verbose_results()
            else:
                for index, result in enumerate(self.results):
                    print(
                        "[{}] {}: {}".format(
                            index + 1,
                            "Success" if result["result"]["success"] else "Failure",
                            result["url"],
                        )
                    )

    def verbose_results(self, results=None):
        results = self.results if not results else results
        for index, result in enumerate(results):
            print(f"[{index+1}] URL: {result.pop('url')}")
            print(f"Success: {result['result'].pop('success')}")
            for key, value in result["result"].items():
                if key == "time":
                    print("Time taken: {0:.2f} seconds".format(value["seconds"]))
                else:
                    print(f"{key.title()}: {value}")
            self.divider()
