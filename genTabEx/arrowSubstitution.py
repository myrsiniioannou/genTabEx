import os


def main(pathToTemplate, PathToFolderWithFilesToProcess):
    dirname = os.path.dirname(os.path.realpath(__import__("__main__").__file__))
    templateFile = os.path.join(dirname, pathToTemplate)
    folderWithFilesWithoutArrows = os.path.join(dirname, PathToFolderWithFilesToProcess)

    with open(templateFile, "r") as museScoreRawFile:
        museScoreFile = museScoreRawFile.read()
        startText = """<Articulation>
              <direction>"""
        endText = "</Articulation>"
        startOccurences = [
            i
            for i in range(len(museScoreFile))
            if museScoreFile.startswith(startText, i)
        ]
        endOccurences = [
            i for i in range(len(museScoreFile)) if museScoreFile.startswith(endText, i)
        ]
        difference = len(endOccurences) - len(startOccurences)
        endOccurences = endOccurences[difference:]

        articulationList = []
        for idx, i in enumerate(startOccurences):
            articulationList.append(
                museScoreFile[
                    startOccurences[idx] : (endOccurences[idx] + len(endText))
                ]
            )

    for filename in os.listdir(folderWithFilesWithoutArrows):
        filePath = os.path.join(folderWithFilesWithoutArrows, filename)
        with open(
            os.path.join(folderWithFilesWithoutArrows, filename), "r"
        ) as museScoreRawFile:
            museScoreFile = museScoreRawFile.read()
            chordText = "<Chord>"
            chordOccurencies = [
                i
                for i in range(len(museScoreFile))
                if museScoreFile.startswith(chordText, i)
            ]
            articulationIndex = 0
            for idx, chord in enumerate(chordOccurencies):
                if articulationIndex == len(articulationList):
                    articulationIndex = 0

                chordOccurenceEndIndex = chordOccurencies[idx] + len(chordText)

                codeToEmbed = "\n" + articulationList[articulationIndex] + "\n"

                museScoreFile = (
                    museScoreFile[: chordOccurenceEndIndex + 1]
                    + codeToEmbed
                    + museScoreFile[chordOccurenceEndIndex + 1 :]
                )

                if idx < len(chordOccurencies):
                    chordOccurencies = chordOccurencies[: idx + 1] + [
                        i + len(codeToEmbed) for i in chordOccurencies[idx + 1 :]
                    ]
                articulationIndex += 1

        with open(filePath, mode="w") as f:
            f.write(museScoreFile)


if __name__ == "__main__":
    pathToTemplate = "books/book-VI/chapter01unit03template_articulation.mscx"
    PathToFolderWithFilesToProcess = "books/book-VI/files_without_arrows"
    main(pathToTemplate, PathToFolderWithFilesToProcess)
    print("Arrow Substitution Done!")
