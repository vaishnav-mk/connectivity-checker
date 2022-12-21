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
                self.verbose_results() if self.verbose else print(
                    f"Success: {result['url']}"
                )
        else:
            if self.verbose:
                self.verbose_results()
            else:
                for index, result in enumerate(self.results):
                    print(
                        "[{}] {}: {}".format(
                            index + 1,
                            "Success" if success else "Failure",
                            result["url"],
                        )
                    )

    def verbose_results(self):
        for index, result in enumerate(self.results):
            print(f"[{index+1}] URL: {result['url']}")
            print(f"Success: {result['result']['success']}")
            for key, value in result["result"].items():
                if ["success", "url"].count(key) > 0:
                    continue
                elif key == "error":
                    print(f"Error: {value}")
                elif key == "time":
                    print("Time taken: {0:.2f} seconds".format(value["seconds"]))
                else:
                    print(f"{key}: {value}")
            self.divider()
