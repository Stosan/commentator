import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';
import { exec } from 'child_process';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('extension.convertToPNG', async () => {
        const editor = vscode.window.activeTextEditor;
        if (editor) {
            const code = editor.document.getText();
            const highlightedCodePath = path.join(context.extensionPath, 'highlighted_code.txt');
            fs.writeFileSync(highlightedCodePath, code);
            const outputPath = path.join(context.extensionPath, 'highlighted_code.png');

            // Execute the command to convert the code to PNG using a third-party tool (e.g., Pygments)
            exec(`pygmentize -o ${outputPath} -O style=vs ${highlightedCodePath}`, (error, stdout, stderr) => {
                if (error) {
                    console.error(`Error: ${error.message}`);
                } else {
                    vscode.window.showInformationMessage(`Code converted to PNG: ${outputPath}`);
                }
            });
        }
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
